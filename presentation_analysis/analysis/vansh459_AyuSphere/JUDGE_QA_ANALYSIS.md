# Judge Q&A Analysis — vansh459_AyuSphere

**Repository:** `vansh459_AyuSphere`
**Generated:** 2026-09-30

**Judge files found:** 2
- `docs\uat\Tech_Security_Guide.md` (17.0 KB)
- `docs\uat\Tech_Security_Guide.pdf` (155.6 KB)

---

## File: `docs\uat\Tech_Security_Guide.md`

```markdown
# AyuSphere — Technology & Security Guide

**SIH26046** · Ministry of Ayush · All India Institute of Ayurveda
Live system: `https://ayusphere-three.vercel.app`
PDF version: `Tech_Security_Guide.pdf` — regenerate any time with `pnpm tsx scripts/build-tech-guide.ts` (versions, the RBAC matrix and signature statements are extracted from the codebase at generation time, so the document cannot drift from the app).

Companion documents: the 7 role UAT guides and `Judge_Demo_Script.md` (the 8-minute storyline).

---

## 1 · What we built

**AyuSphere** is a working, deployed clinical trial management system for AIIA's Ayurveda trials — not a mock-up. It covers the full trial lifecycle (draft → IEC review → CTRI registration → active → completed → locked), participant screening/consent/enrolment with permuted-block randomization, template-driven e-CRFs with electronically signed approvals, a complete pharmacovigilance loop (MedDRA/WHODrug-coded AEs, configurable escalation deadlines, CIOMS-style reports, safety-signal detection, DSMB packs, NPvCC spontaneous-ADR intake), monitoring visits and data queries, protocol amendments under IEC control, and standards-based interoperability (CDISC SDTM/ADaM/Define-XML and a live two-way FHIR R4 API).

Seven enforced roles each see a tailored workspace; every mutation is validated, permission-checked and audited in the same database transaction; and the whole system is gated by **319 automated tests** running against real Postgres. It installs like a native app on phones (PWA), and every displayed date is pinned to IST regardless of where the server runs.

## 2 · Technology stack — what and how

### Frontend

| Technology | What it is | How AyuSphere uses it |
|---|---|---|
| **Next.js 16 (App Router, Turbopack)** | Full-stack React framework | Every screen is a server component that reads the session and renders only what the role may see; mutations are server actions, so clinical-data logic never ships to the browser. One repo, one deploy. |
| **React 19** | UI library | Server components for data-heavy pages; small client islands only where interactivity needs it (forms, Sphera panel, toasts, mobile drawer). |
| **TypeScript 5 (strict)** | Typed JavaScript | Strict across app/services/tests/scripts; DB row types inferred from the schema — a schema change breaks the build, not production. |
| **Tailwind CSS 4** | Utility-first CSS | Implements the design system (glass + clay tokens, one font, two text sizes); a static design-qa test fails the build on violations. |
| **framer-motion** | Animation | Small approved motion catalog — decorative only, never load-bearing. |
| **Recharts** | Charts | Dashboard KPIs: enrolment progress, AE severity mix, portfolio charts. |
| **Live badges (fetch + events)** | Dependency-free client refresh | Live unread badges and toasts refresh via plain `fetch` on navigation and a `refreshBadges` event — no data-fetching library; unused deps removed (T6.12). |
| **PWA (manifest + install banner)** | Installable web app | Standalone manifest; phone-only banner — Android gets the native install dialog (`beforeinstallprompt`), iPhone gets honest Share → Add to Home Screen instructions. Desktop/iPads never see it (incl. iPadOS masquerading as a Mac, excluded via touch-point detection). |
| **IST dates (`src/lib/dates.ts`)** | One timezone truth | Servers run in UTC — bare formatting shifted IST users back a day around midnight. All date renders go through Asia/Kolkata-pinned helpers; a static test forbids bare `toLocale*String` calls. |
| lucide-react · clsx · CVA · tailwind-merge | Icons & utilities | Iconography and conditional class composition across every screen. |

### Backend & data

| Technology | What it is | How AyuSphere uses it |
|---|---|---|
| **Neon Postgres (serverless)** | Managed serverless Postgres (WebSocket driver via `ws`) | The single system of record: 25+ tables — trials, sites, participants, CRFs, AEs, signatures, amendments, queries, audit events, guide threads. |
| **Drizzle ORM + drizzle-kit** | Type-safe SQL builder + migrations | Every query is parameterized from the typed schema — string-built SQL does not exist in the codebase. Versioned generated migrations (0001–0009). |
| **Zod 4** | Runtime validation | Every service input parsed at the boundary — types, lengths, enums, ranges — before any logic runs. |
| **Vercel Blob** | Object storage | Consent forms, documents, doctor-note images under unguessable UUID paths. |
| **In-process TTL cache (`src/lib/ttl-cache.ts`)** | Dependency-free response cache (ADR D-030) | Portfolio aggregates (45s), search (60s), Sphera config + fresh-thread replies cached per warm instance with stampede protection — audited responses and live badges provably never cached. |

### Auth & security

| Technology | What it is | How AyuSphere uses it |
|---|---|---|
| **Auth.js (NextAuth v5)** | Authentication framework | Credentials sign-in, **JWT session capped at 12 hours** carrying id/role/site; built-in CSRF protection. |
| **bcryptjs** | Adaptive password hashing | Cost factor **12**; also re-verified on every electronic signature. |
| **node:crypto (SHA-256)** | Hashing | Every e-signature stores the SHA-256 of the canonical JSON of the signed record — tampering is detectable. |

### AI

| Technology | What it is | How AyuSphere uses it |
|---|---|---|
| **LangGraph + LangChain** | Agent-graph framework | Sphera is a StateGraph: loads the user's persisted thread, injects only THAT role's knowledge, streams tokens, saves the turn to Postgres — memory survives refreshes and devices. |
| **Groq (ChatGroq)** | Low-latency LLM API | Powers Sphera. Admin pastes the key once in Settings (stored server-side, serves all roles); env-var fallback for dev. |
| **Anthropic Claude SDK** | Claude API client | Clinical copilot + doctor-note extraction (image → structured **draft** CRF, always human-approved). |

### Testing & tooling

| Technology | What it is | How AyuSphere uses it |
|---|---|---|
| **Vitest + PGlite** | Test runner + Postgres-in-WASM | **297 tests / 47 files against real embedded Postgres** — RBAC denials, audit atomicity, signature refusal, randomization balance, export formats. |
| **Playwright** | Browser automation | Live E2E sweeps against the deployed site + the PDF generators for these guides. |
| **Faker** | Synthetic data | Every participant, CRF value and AE in the demo DB is synthetic. |
| ESLint 9 · tsx · pnpm | Lint / script runner / packages | `pnpm verify` = typecheck + full test suite; nothing merges red. |

### Platform

| Technology | How AyuSphere uses it |
|---|---|
| **Vercel** | Auto-deploys every push to main; Vercel Cron drives alert/deadline sweeps (bearer-secret protected). Cloud-based per the PS. |
| **GitHub (trunk-based)** | Single main branch, small verified commits — the repo is itself an audit trail of the build. |

## 3 · Architecture & workflows

### 3.1 · The life of every write

Every clinical-record change — enrolment, CRF entry, AE capture, approval — travels one pipeline; there is no second path around it:

```
Browser (role sees only permitted actions)
  → Next.js server action / API route   (session from 12h JWT · HTTPS · CSRF)
  → Zod schema                          (invalid → rejected with field errors)
  → RBAC assertCan(role, capability)    (denied → RbacError, nothing executes)
  → Service layer                       (state machines, deadline rules, randomization)
  → withAudit() transaction             (mutation + audit row commit together or not at all)
  → Drizzle ORM → Neon Postgres         (parameterized SQL; audit_events is insert-only)
```

### 3.2 · Sphera — the AI guide with memory

```
User asks Sphera (leaf orb)
  → /api/guide            (session checked; per-user thread loaded from guide_messages)
  → LangGraph StateGraph  (injects ONLY this role's knowledge — can't describe screens the role can't open)
  → ChatGroq              (key from admin Settings, server-side; ne
... [truncated]
```

**Headings detected:** AyuSphere — Technology & Security Guide, 1 · What we built, 2 · Technology stack — what and how, Frontend, Backend & data, Auth & security, AI, Testing & tooling, Platform, 3 · Architecture & workflows

**Question-like lines (contains ?):** 1
- | Question it answers | "Can the wrong person get in, read, or change this?" | "Should this data exist here at all, and 

---

## File: `docs\uat\Tech_Security_Guide.pdf`

```markdown
%PDF-1.4
%
1 0 obj
<</Creator (Chromium)
/Producer (Skia/PDF m153)
/CreationDate (D:20260914190400+00'00')
/ModDate (D:20260914190400+00'00')>>
endobj
3 0 obj
<</ca 1
/BM /Normal>>
endobj
7 0 obj
<</CA 1
/ca 1
/LC 0
/LJ 0
/LW 1
/ML 4
/SA true
/BM /Normal>>
endobj
9 0 obj
<</Filter /FlateDecode
/Length 2423>> stream
xZ͎
S Zff{ލ<u@@TRmCcZMTSJ_uBս|tV(*FPT}I9z>]jHVj(EB_|%

^*ZN珗Iaf<"^Xt/.՚	QG }@uMcsЈ**kB*vN#xZ+5X 022tLD堆0'0!xV[X+nHh}fn[c.ay@ 'tߑC457oKc`V
khGANΛ
6Uĝ|5*$_ qmB`&Jv[Ҷ\-\?TRJFW^-/J,$>d|	˪9 Cu)2Vq;|BvmUg22I O0ߔe!?4W#8nXYFKg eu(WfEW-pS֍pǺ8<	"bJҰ3p2
-d0GT{^ښ8s;]͆hQx `"*  2 _{ 1{W~t>e#9Ge=|dz2=,w˵i8;ajWPF2ӳu2ʳm#00/#Z_|wHerxD?G*6uq*䨀/k$	okZzU
jUW	֙y|:sR~ICGa@43XocEjQib[cS)
P% ̊DԦ&R>S.T"QMPW
ܔV5"	KX
@Pc[zQBVîP]A.`E2w@>*v	>M9M],EtҸcS[guiE%#P"=.,+uY"%*i=U:]k*{ObfhKcצuH[UPVIطLi o5ڀIW
@#ؖEOXY>"-`edt-%)hK3uM"cë$L;MFί#F&Zgn6eFe)
.Ef89%e<⪬R*d[l򣨟x${3e-mT3҆ý`YaE&yXdƛhaf,S
kmT=|}dEgƛi4-$G%#Rj-hӴMmX԰MlLi8&rme 腀
(HmxJ+e=0ҟVvYDdmieZep$YNiΰ=u-֩\:iWr։=_X"к6&7H.Eue4_*y	V8.ֳ<y?3x>WwR]xB|vovoWݚ/9|o3|9nr[j&-WG(^<Q:=Y/j0s,PhJ
?RQ>(T-s-^-RE2χ
l"кb
MR)6/VqH_K5}!.\Duas_ВҵR_%.4Jjp@B]~fc \.<$9f]p IF9Om;JgYg)S'=Z 	L6RdyoPہJ2mK_VQf75gcε>iFEB3-f#؉O
E7yFgb>9SGT	w(}\43k{grN-
Nr9K&
,3A{=y]wR5Fͮ-ǎNK
q	7_@}3iܛ {!@n;Hw}%5}AzΟ_sjݛG淚MG'IAzSw9-%:Rgo۫@ʱyhjdVl|<GGjD?^ʫ|
I8W\͖Ϝ>4xC@٠e.@1Ge6xӃk/9;^j;/36͗oenq\&7Y
R]U%e$n{[emn{{֏Vbo>ι=W`a3H1\_/^
endstream
endobj
11 0 obj
<</Filter /FlateDecode
/Length 3978>> stream
x\݊6B*T ,s;YB}X,Kr>ut20tlTWlK g$kb~茣ă6L3h}4`(De8l^C0y~Mdl2cȃmvǯS%lzSc6L5zjm&&$<bzVff<3Ƕ);6vjm-ی6F֣MmeGVMѦ69ףhi5Ziko_^p3AϿ  榟@W " 6?/` R`` | =s#Sf#
UZjbY<n2Ʌ۴  "'buy^^ϋ7?:Nwv^;@ x+$WxdemT8M<=ko<W(VPRD^^Ci`oHeȃ0f8O3aw^̘W 2@,Iq"q<[șWYtpOoRIMeLNcPcj_glu]59Ep!"`P
?p9^^wRa~f絅ߖmfe, T&N+R)ϫUF+(G(T~^7E*eq˂S FRdU0s=I@lU&%M3w2Ft%1w8#.{!HRIjyDiZi;1kZYy&&B7/{lcaSKӘ&8UiB/Eze
Իɤ$\x/mY6{.AZR*KgZѢgq[jt1=ַJz@aeX׻,ElҺUݖkr܄$˓e0)g6bxbi/K3Zt#Us<\탈d|f%,nbqKXM
s*	P0j\lg2ĉwuG2^
YzT?btW&,3BECQF)ϿO]CjF`2`}ZZ[UTuA
ߚ~'m%N|)KP4јf*,ǟ(+P]A'ZMnӎ4%b0,7.9&\_ͳb-isRx떡r
-e s?\dP~um2R]y9Gu}5d߄
r|MRnrRN}f*ICu-՞ܳek}^$5Y"kbOk)YDӼP潗;Ru׶Y=S	!O-RyJk.ɇE}bA~zC)-_j1?OpқV/[2r֙Eb>uX1AU:O^9
|Z^_ʧ;545n0q9eIc;;\T3SMy2+s1_oDS+&]6Ǩi$\uU`
Y3
} *#D\z-
"<H[YNs
ǋc,W[F9UJHy/`(|:ǥu]cǵLa?n\ĥ{v"ˣl"%KnN3Ea>	Ȋ-KxX3> vGKy]t(C}KnP2VX2Nr\xNYI*V)rKJ!ߚ`1#EVl<TPj7c`JmfN1ŔvȢH@K<R wq\@brD!'&bwP)WuC](d_Â(-mzFZ8o"1;BFE=E϶eq/j"<V0ֱM3/>yU,0gx;L 6&Qf&6YzҘ˭3VH`IUj
)D+n59*mBz5D19
ƍ6#go+y{X	&fkbAqtZQ8ՙM #t3D=@(r;w"/E
"ա"hI&VpRv[@FcقNH{U*JLbK7*IJVz4	.< ň2~4G/uYfم[>8diU	CvKTe1O3d9e'	9ͪk*L`x
Plʀ .q=ct·@nm5
D) 'ĶFE$p"XuŎcUlIT9Te*5Љܡ]`y`'J %oUʂ[O;IOV~Q	/W;ȫ)ZU<cV%m _I4\
^!>YjC蟼[
XxK@H*I:ԡ_U`906hzZB|(a=BsE+VǢRCiiʼÆ  _,VcٙMzbdt|ধJUuh[/rI
PO
F[.c+-uc=;<۶eݼGըwAdnSj?VwiZqM@g1(rqhW`}^ yn![F'?0m<4N%Cg<k1\o鉽PIFouw6⚤
,Vn[	΁`kP!x qRcQt}J\񹻦x`$:{.P׽St^T
n7fGjQmc>Ֆus?U~&CD{5
sj{ 67ឃ߹g/FMuaGufuVGmXc`wN,#ȝ4ӟTתuj]j6G7&!xZh&!&1LRg[j><f>bϱJfb#`o#'uM
T=|=q֢th=JC)fcN(+ExE&SO|@a35niM)
)r#BOݿx?9ն8Vu!_?OS. =_kT#w`<\ճ28ܟϩ͟@4.w~S3R
CwYǀ:T=b9Q*8s׿q:Υf?OfxW-ռY9ýol<gz`_NFxr_伪O<b6=vZν㵚+qD;~Z~T
{h8vCKޜPk/:)w'Ljh`($Vqnٔ뮀QSXcap]Vb뇓";p֮]W(ϜǺ1
1~hD&_PHuoI@|v&A [{?fjsr
|5kntիhY5"?:}Ѓ*gEK*/ O>'p@*R~|e:bu\'7|A/7SO+z>v*k \
0''}\w\<};
$8!.ӏ-W-i:oHXwA#wu<"{S}/y8yC)~P KإwzmFz^!b
endstream
endobj
13 0 obj
<</Filter /FlateDecode
/Length 4121>> stream
x][ܶ~_a^@PǱ@@(I?PhWx$}+
s6~May囡!;;SS<]~yk"aDٸi㟗eGUwIaHn0٥82Ӱix(8q_/-ݚ\B.mT\pƶUocӺ[۫(𦷱mش7ml[66{-ml[66{-mƦuoW	Moc۪iۭm 2&DJQ?h\$s'#0.(vn<Kl\Gv׶4nT8M~/_.#2|n|@Y×.?X_/x%ֆ0}b<!h_9~(Dz69|p|3~I&D/iZIH[W4:?ӕ~b8<px=Mc9N6r}(l.IGiԿyfҴsk4c66{FQ!s'dy{\6F+A64aM[N[ZQM3MP63<5MUw_$gǇiS򣷎kD_8
9;Yħ/b2ḱ	qbrNN|=AF
ep4HK7x!dC*`}%-ÍN!YXb
8}S\|[XUMÒغwѾL,8AxJ3:|g?^(_opjӾ8Ʉy2e[MHF!w q#`8ۗۇiDNpl!l}Ge!O]]pb+;Y+t=҅d!F`SXWqg
"gy&XR.$ov&cQzڈ.c!sUQjP(XL&1mٔSZuclev)oqCzcD/\kUg&LRvg43G3	rhG^G 񜤒I\!-24;{d9/޵'tx6l>O!*ۢXL]ަ
*ֻ(j*X;/E[w?7(d. *B}6EY#$֣A	.&
5\	I/Y27}:u4,3e-b8ݢ185 <TTIBvل]2E<>vյ8o`$qw,[pNborqFWE$cs{+5l?MLʖ4i٪O|CY
~F4>_Њ۠y-
>MYWhBTw>u0Ǡ$۪
>֨[Sqv5)o~r1%
 %TjbDt-4j	fM6m
g܎v}m;7H)\mO]
xp3
LPhƛў P*&z3'Fs'*t]޻6D4n~nNzrݣgHgχDԠ= TIOxRuDJ7TCG:UQfs '"pp0IV@TV$Rm+EXJ}ǄT+T=cSP<A"I)Z+؊_Bd'&mN*!<47+{0`
F$űhч1>xzۜbyh,fBŠvQHrWAF	`&q^xj%c5+ۦ&ݲ)3
g!#S` VotyиSjҀn,p7Bgx}dLhԞ
Qwq 3.#²+[fŽkVEdxy>ONj&=į*+Lʔ&tm \)x(>vEvT]d.n6`Jj_栗ijYwĎOB2(0ɑ(ñ^pm}zocLSg%>)qMmQDEm4j)oSy֏!9WueECg( Huq|AGcЦ(:g  "N =oWF6{__7GM;'4\h;G=6\XXPFf 5jE+n5=RQX:B[_1izWd
.UH|Y#>`b3D| kKayhX"aDZ0I0'X_]Pz>-*<C󎍷AAV c<VMNwd̻H_$C!I0P[]
aƆq:Dto1zO>ϪzJ~Aƃ&!<HS&	$O9!Fu$
t)#=z~'˫۬ĜBC[bV58 np!Q&{>>P;[AA
<P}C_@h9ͥ6/P^@gz/8zu$#8;]aTӫ<OIOw5ċ\ݡvtsl>JS?(d.g9v
Cɚzgk>&1J㰞$h+iz}EgTU?1*:6
9:шcC1L߂ǺCqR.E:z6kiP]Z.]o(	Zpρ\\FD%agQ;ox%|	V>@З|X>C8x
7".Ȗk@.d˖rޭ
@C]HpKE)}|/6{rPU1qE<4XRx4ԿՕP+
0QX zícwz[_f!7kJjmG"ʮ:qddq!ǥP:w6n8a4UX^z(!'3sVE󃋯dNS/ya7E}(}__ Hu^?4RM[c'WY"QeS\\"\lv9]S!q؁!T=A7ZklJv9n*sr!⎂sv+W$$jEfyBNQ6kx:rL1뙢BگxnsBسԛ3U&f;C1Dl=js1zq̢s؇ms\lLi'%h?VIɝ\9\
8+Va<?&Jnع[7
.q4XD"G	qXZuH-z_ePOGޤ`\Ci68CD]i8[cDs\Z_ӯag՗g{S>`^c71\'T4懝P%bѮY3t6ZkQzn%łO=<V'~%0AkQ3T=ᵖf*Tqo/:n'{ju3$ʻ(o(g`}MJ$OFA仯\NQrJoQe+58\a~&qgvV_m#[`PJ`Rn[^qo!GOf5-c"*Dw?>}ag^GC	3i&eOn"Ho>>swāNb:HT7D"}2+V[C̦u;Au$V
+r|TA~O- Vj<
endstream
endobj
15 0 obj
<</Filter /FlateDecode
/Length 3890>> stream
x]ێ$
}ﯨ EJ(?;X 8ꮋOUVӞcɭ%"/rwUj?N]b8jp!Ͽu9q
XC}WD.iԹB9uNvj?byX+ȥ-r4Q$Ц~lGr=Z߶oZvn{=Zr5Z߶oZvn{=Do[7-G;-mhy4Es)uTkWvJG:.Ç}CcѩQ\9?1綊}[jp}rm9b,zs[5yzt.I.g:.Oyʢ{sGtI%%-SGx.L94k;0TsGr%QÇQ=xCRUx
1>wųE,dvbO䇡5Ϳ<ͬ"_MB'$΅\Hx8rcB|pB͔Y+G0/ѹ]18oe5%v"(3W4wY۰1aJϑÌNd8,FN{Ka]q,4tL8#+^-ı'}AIY̜`#c˸TR|ߐ8.tEJQ؇m:=
U'5JJ8O#a2!:&D?wCޱ<#b1Myv(׬Mo\mV۩?y).<o%!}ӏ>RçHȳ2!o) 7Ik!C]`y}OX|iX5E *cƬi`},ˑj
2	pxarK,W.I[	N~a΃{l<-(G.s}v9QĴ߬دKǰZ;پZ 
+Vʨ\a9!wh
cΪߓ%`Ƨkhg7[1V{ҬGzhEVO")'>o1d7ˈ}Zvص3A[nݼDˇ^78nhC$JCZK{=v9_eB:gt;7GD3݉-&ѧł\x)Ĳat/隫XK&\LfX=n;|@$tyAi}a	
b6!pC!/ۭ-q0J;'e$ N7'	y mO*@`QPڭ
ۍ
Mu tc
	0ucvxsD.3_)A.QVcw9]e_d)7OKjG񹸈(Rٻmpߞg9-VUr
ZS`C9
נ*gSos13T#(ag3g~|/#yO_|yVOZ.3&riWFCBĚ
&^5'Γip[E=`v
wm))0<yׂ&RLIX}2߉0zn2أ֕&oP98{DA1xDC_㤾1@ t9P'Ʌཏol	5>K`Zێ6"zW TF.:k'[ba$<rviMea!<nO'gD//ԥEt s\W9i G4gS֬ʓSE-{J2P{CQ`/%_d%V*0Xbic#ی	L+ECq,q%o8Pˎ
*"eHyH4+䍌R*i/ցx"Cct{֌DCq^@EBd6x_q!ꀳCpcI0lL;@\y'TI8(P7
EoY95|-JhJ,ĺC;ǁ=p&(I	e<,tG/;~yǜ'ԁ~#}8;P\3gx*vd'o@ 0_aFx8bzp9J!A"+-fn ua0I^Td{PE+DRbc<H&bk0{.C^5LĖqSfQB-Ygw<m-six\1RȴSi#H;_l[4.R9V`=J5{ӆaP|c?U
J&^*czLVc
12iGP;S|zk?-
ZVO*C$حz{L1dkˁy{mI&q=RK\;ǉGآqŎ+o䩴B^{_.ϴo.Z$32f?B.Tq:L#%
uPc|N$o-IpxL%R`>WQ֯᪰NٻT-NMͲJG#B(
$.N.3S$b}:R8eɷRD
)[^͋3=ťEˍx0-b1R|Zg'$[T|F+CGWT%ӎ_@!lY_eq^+?ӪIVUB&SUB5#G>hlGhQ!rHȜԳ
i5Ω_<=_k;Ɔgڗe{qG׮[jڍZۿKMm@f^ɂv]^3;P\ ʱ@lX廵Ro\?W0cf`,|J"58j,gF!LX01fޥ9mՅ9ŝ՞3P:޴jpPp3ˤ,63T1)vk6ZWBcPE;b-ӛÈMڽ
/09 I5taV֮i4	s`CeyW/B>H|7[d9ueڟO3'GeZZTX\A|7Lan AHUx`Ct&=8IH"YhXlDvr"÷I<Ol9ING8zP6]֢'o4u~yV;::j2=lRgO5,7|,;o49^
Ci(-(<np>]!sjc">57xWe]> 
*/cj{\+aE^X(Wǀ50AɠD3*vFchIU^UEFhc'G4< ;WqDH{ Eu+b̕"̷/\RxOf6bi#;Z5↩]5O wpMkKi\^O0yNћy{XA73
... [truncated]
```

**Q&A pairs detected:** 3

### Q1: =Y/j0s,PhJ
?RQ>(T-s-^-RE2χ
l"кb
MR)6/VqH_K5}!.\Duas_ВҵR_%.4Jjp@B]~fc \.<$9f]p IF9Om;JgYg)S'=Z 	L6RdyoPہJ2mK_VQf75gcε>iFEB3-f#؉O
E7yFgb>9SGT	w(}\43k{grN-
Nr9K&
,3A{=y]wR5F

**A:** ~ĝIc1Kg,)NY&ʪ>799DɎnNFmD֢k݅'OI+Sی~o+I\5-
5JHD}3h[i$j X_hglr/J%2M}ў^|tQiރON2\C`18*5Uh!X/JM>(_>XFukEVVvD}
3(__)6p*+U0Xx*m/*M{J,3 FAք4<6w͵.Г;93șML
Cw&F(R:͎\bt:[/|ck)1TnPR
wD©b!eM64ںN%1(3|sB9;_!5D"-/Tٰг 	F@42U2֐5{D#3)!Hym[q]_`;؏M'fv2nQ`B;RA!k}{ #C4!ǰ<D1P6!v{
"GnϹfNY0n)#5[i(}*c=GK@KEkjrWWP5|7^s%YewO]_-]p?h+_Pn$PKEV־QgV2ƪC0
- **Category:** AI
- **Evidence:** Check `analysis/vansh459_AyuSphere/REPO_ANALYSIS.md:16` (Audit) / `ARCHITECTURE.md` — actual code vs claim.

### Q2: F$8$ĦHT%%.?γILǵIBaہdQm
'Qyc%:OƵ$ĦzC+abT>
$T	MRv7B>(shnΨ-O%hG Z<j-5D%^"NKp2~umumڶ4=h(1IB!
ҋpSZ pH<hnv
PrŭSU-

%;ʮOrRZɐ*DphpUp{ᮍWw1%bnNodQvyuS̆S$:N9jڃã{-6/

**A:** LYvƅ8FsuS}B(q*/!5a)< Ѻj(uPO-&lHQϧs;xr}L0CHV-TtWSh j;,99M=6HPςpg.$R$ Y=I!U/H4_
4tz ]=
^
!C
|ݡd@OWȄ^zBO_d@oQ	ϐϐ
yϐ0?A?A>?A ԟ?B?B?B1A }TA r@Az
dT0H2{0A%UAP~0;I'a(Ԩ'
F'aPO@5Ԫ'`8ROpzjJooa$oaV0F=WX8\PGaƫh~c(cPa1Sԯ_QNWD"կ`
Q"F
\Kר_~	3a%̂Q
ԣ0«azhz%0_|
uG`P>RJ=KOaXJ2X0,CnRJY=`9\'X~VsX
p9M^n
g
- **Category:** AI
- **Evidence:** Check `analysis/vansh459_AyuSphere/REPO_ANALYSIS.md:16` (Audit) / `ARCHITECTURE.md` — actual code vs claim.

### Q3: #B;,rJX
G@y|CwEy]iEXpNy?=rڅG\iAeV~S~S>,@\/`rA24rFh
,cc
M!Yh;r'[݈LD1ۨlqNMrh</:txsoE/`W?yI%tk?·zUs}MBW&d Cl9M"hꛦ6l`}	qLyOLXT8FР7C`5Ut&
bLFQS{p ܹswV>ޡ8cޑ[o]鉛o^

**A:** jmI2|!SH6"HJdzFbO9:޺4ԳZ$DEr;PV93D/{1mD.?Rn~s\k__nn{m[pgmߵOl`O'
w=E:pDpu>r7vű5:&J<%F<e'
/\؈#^U$Ƣ=ݵܢp43]M{3Wp
!݅1\0i-&Ddd'IkLb}3bT`tSkپ}Ҭ2_k+ϕUzOҍ.)a9}BClJDQD5W+uL^X=پhCþJaF畆λXp+O*Z~&ogS6NaOaG;KťF\l ^r=@4QHnrN&G[HL6HT,h_I>3NcKeĵB_!0鯔2+xBIO+w[ʟ ʉ`P,SZ#y!;:VD(i!Fa6ؓdE6M}C"0D7grC.nѣ?z	9߬456#xHwkzBNljǫ_G%IVb@YٹPB
- **Category:** Unknown
- **Evidence:** Check `analysis/vansh459_AyuSphere/REPO_ANALYSIS.md:16` (Audit) / `ARCHITECTURE.md` — actual code vs claim.

---

