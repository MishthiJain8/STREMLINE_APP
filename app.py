import streamlit as st


st.set_page_config(
    page_title="Mishthi Jain | Software Engineer",
    page_icon="MJ",
    layout="wide",
    initial_sidebar_state="collapsed",
)


st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --ink: #101114;
    --muted: #686b73;
    --line: #dedfe3;
    --paper: #f5f5f7;
    --card: rgba(255, 255, 255, .82);
    --blue: #0066cc;
    --blue-soft: #e8f2ff;
}

html { scroll-behavior: smooth; }
.stApp {
    background:
        radial-gradient(circle at 15% 0%, rgba(0, 102, 204, .11), transparent 26rem),
        radial-gradient(circle at 95% 20%, rgba(122, 92, 255, .09), transparent 28rem),
        var(--paper);
    color: var(--ink);
    font-family: "Inter", -apple-system, BlinkMacSystemFont, sans-serif;
}
.block-container { max-width: 1180px; padding: 1.1rem 2rem 5rem; }
#MainMenu, footer, header { visibility: hidden; }

@keyframes enter {
    from { opacity: 0; transform: translateY(18px); }
    to { opacity: 1; transform: translateY(0); }
}

.nav {
    position: sticky;
    top: .8rem;
    z-index: 10;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1rem;
    padding: .72rem .8rem .72rem 1.1rem;
    border: 1px solid rgba(255,255,255,.9);
    border-radius: 999px;
    background: rgba(255,255,255,.74);
    backdrop-filter: blur(22px);
    -webkit-backdrop-filter: blur(22px);
    box-shadow: 0 8px 30px rgba(0,0,0,.06);
}
.brand { color: var(--ink); font-weight: 800; letter-spacing: -.04em; }
.nav-links { display: flex; align-items: center; gap: .35rem; }
.nav a { color: #3b3d42; font-size: .82rem; font-weight: 600; text-decoration: none; padding: .55rem .7rem; border-radius: 999px; }
.nav a:hover { color: var(--blue); background: var(--blue-soft); }
.nav .nav-cta { color: white; background: var(--ink); padding-inline: 1rem; }
.nav .nav-cta:hover { color: white; background: var(--blue); }

.hero {
    min-height: 75vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 7rem 0 5rem;
    animation: enter .75s ease both;
}
.eyebrow {
    display: inline-flex;
    align-items: center;
    gap: .55rem;
    width: fit-content;
    color: #41444a;
    font: 500 .76rem "DM Mono", monospace;
    letter-spacing: .05em;
    text-transform: uppercase;
}
.dot { width: .55rem; height: .55rem; border-radius: 50%; background: #24a148; box-shadow: 0 0 0 5px rgba(36,161,72,.12); }
.hero h1 {
    max-width: 1040px;
    margin: 1.4rem 0 1.2rem;
    color: var(--ink);
    font-size: clamp(4rem, 10vw, 8.8rem);
    line-height: .88;
    letter-spacing: -.085em;
    font-weight: 800;
}
.hero h1 span {
    color: transparent;
    background: linear-gradient(100deg, #0066cc 10%, #7654ff 65%, #ff4d8d);
    background-clip: text;
    -webkit-background-clip: text;
}
.hero-copy { max-width: 720px; color: #4e5158; font-size: clamp(1.08rem, 2vw, 1.35rem); line-height: 1.6; letter-spacing: -.02em; }
.actions { display: flex; flex-wrap: wrap; gap: .65rem; margin-top: 2rem; }
.button { display: inline-flex; align-items: center; gap: .5rem; padding: .82rem 1.15rem; border-radius: 999px; text-decoration: none !important; font-size: .88rem; font-weight: 700; transition: .2s ease; }
.button.primary { color: white !important; background: var(--blue); box-shadow: 0 10px 22px rgba(0,102,204,.2); }
.button.secondary { color: var(--ink) !important; background: white; border: 1px solid var(--line); }
.button:hover { transform: translateY(-2px); box-shadow: 0 12px 28px rgba(0,0,0,.12); }

.section { padding: 5.5rem 0 1rem; scroll-margin-top: 5rem; }
.section-top { display: grid; grid-template-columns: .7fr 1.3fr; gap: 2rem; margin-bottom: 2rem; }
.kicker { color: var(--blue); font: 500 .73rem "DM Mono", monospace; letter-spacing: .08em; text-transform: uppercase; }
.section h2 { margin: .7rem 0 0; color: var(--ink); font-size: clamp(2.3rem, 5vw, 4.4rem); line-height: 1; letter-spacing: -.065em; }
.section-intro { align-self: end; max-width: 590px; margin: 0; color: var(--muted); font-size: 1.02rem; line-height: 1.7; }

.metrics { display: grid; grid-template-columns: repeat(4, 1fr); gap: .8rem; }
.metric, .card, .project, .experience {
    border: 1px solid rgba(0,0,0,.07);
    background: var(--card);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    box-shadow: 0 12px 34px rgba(0,0,0,.045);
}
.metric { padding: 1.35rem; border-radius: 1.3rem; }
.metric strong { display: block; color: var(--ink); font-size: 2.45rem; line-height: 1; letter-spacing: -.07em; }
.metric span { display: block; margin-top: .65rem; color: var(--muted); font-size: .76rem; line-height: 1.35; }

.experience { border-radius: 1.7rem; padding: 2rem; }
.exp-head { display: flex; justify-content: space-between; gap: 1rem; }
.exp-head h3 { margin: 0; color: var(--ink); font-size: 1.5rem; letter-spacing: -.04em; }
.exp-head p, .exp-date { margin: .3rem 0 0; color: var(--muted); font-size: .84rem; }
.exp-date { font-family: "DM Mono", monospace; white-space: nowrap; }
.impact-list { display: grid; gap: .7rem; margin: 1.5rem 0 0; padding: 0; list-style: none; }
.impact-list li { position: relative; padding-left: 1.3rem; color: #45484f; font-size: .93rem; line-height: 1.6; }
.impact-list li:before { position: absolute; left: 0; content: "↗"; color: var(--blue); font-weight: 700; }

.projects { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; }
.project { min-height: 300px; display: flex; flex-direction: column; padding: 1.7rem; border-radius: 1.7rem; transition: .25s ease; }
.project:hover { transform: translateY(-5px); box-shadow: 0 20px 48px rgba(0,0,0,.09); border-color: rgba(0,102,204,.25); }
.project.featured { grid-column: span 2; min-height: 330px; background: linear-gradient(135deg, #111318, #202634); }
.project.featured h3, .project.featured p { color: white; }
.project.featured p { opacity: .7; }
.project-number { color: var(--blue); font: 500 .72rem "DM Mono", monospace; text-transform: uppercase; letter-spacing: .08em; }
.project h3 { margin: auto 0 .65rem; color: var(--ink); font-size: clamp(1.5rem, 3vw, 2.2rem); line-height: 1.05; letter-spacing: -.055em; }
.project p { margin: 0; color: var(--muted); font-size: .88rem; line-height: 1.6; }
.tags { display: flex; flex-wrap: wrap; gap: .4rem; margin-top: 1.2rem; }
.tag { padding: .3rem .55rem; border: 1px solid rgba(0,0,0,.1); border-radius: 999px; color: #575a62; font: 500 .64rem "DM Mono", monospace; }
.featured .tag { color: #d9e7ff; border-color: rgba(255,255,255,.2); }
.project-link { margin-top: 1.25rem; color: var(--blue) !important; font-size: .8rem; font-weight: 700; text-decoration: none; }

.grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: .9rem; }
.card { padding: 1.5rem; border-radius: 1.5rem; }
.card-label { color: var(--blue); font: 500 .68rem "DM Mono", monospace; text-transform: uppercase; letter-spacing: .08em; }
.card h3 { margin: 1.5rem 0 .7rem; color: var(--ink); font-size: 1.2rem; line-height: 1.2; letter-spacing: -.035em; }
.card p { margin: 0; color: var(--muted); font-size: .82rem; line-height: 1.6; }

.skills { display: grid; grid-template-columns: repeat(2, 1fr); gap: .9rem; }
.skill-group { padding: 1.4rem; border-top: 1px solid #c9cbd0; }
.skill-group h3 { margin: 0 0 .8rem; color: var(--ink); font-size: .82rem; font-family: "DM Mono", monospace; text-transform: uppercase; }
.skill-group p { margin: 0; color: #4e5158; font-size: .92rem; line-height: 1.75; }

.fit { display: grid; grid-template-columns: repeat(3, 1fr); gap: .9rem; }
.fit-card { padding: 1.5rem; border-radius: 1.5rem; background: var(--blue-soft); border: 1px solid rgba(0,102,204,.1); }
.fit-card span { color: var(--blue); font: 500 .68rem "DM Mono", monospace; }
.fit-card h3 { margin: 1.4rem 0 .6rem; color: var(--ink); font-size: 1.2rem; letter-spacing: -.04em; }
.fit-card p { margin: 0; color: #596370; font-size: .83rem; line-height: 1.6; }

.footer { margin-top: 6rem; padding: 4rem 0 1.5rem; border-top: 1px solid #d4d5d9; }
.footer h2 { max-width: 850px; margin: 0; color: var(--ink); font-size: clamp(2.8rem, 7vw, 6rem); line-height: .95; letter-spacing: -.075em; }
.footer-bottom { display: flex; justify-content: space-between; gap: 1rem; margin-top: 4rem; color: var(--muted); font: 500 .68rem "DM Mono", monospace; text-transform: uppercase; }

@media (max-width: 800px) {
    .block-container { padding-inline: 1rem; }
    .nav-links a:not(.nav-cta) { display: none; }
    .hero { min-height: auto; padding: 6rem 0 3rem; }
    .hero h1 { font-size: clamp(3.8rem, 20vw, 6rem); }
    .section { padding-top: 4rem; }
    .section-top, .projects, .grid-3, .fit, .skills { grid-template-columns: 1fr; }
    .metrics { grid-template-columns: repeat(2, 1fr); }
    .project.featured { grid-column: auto; }
    .exp-head, .footer-bottom { flex-direction: column; }
}
</style>

<nav class="nav">
  <span class="brand">MJ.</span>
  <div class="nav-links">
    <a href="#work">Work</a>
    <a href="#research">Research</a>
    <a href="#skills">Skills</a>
    <a href="#apple-fit">Role fit</a>
    <a class="nav-cta" href="mailto:mishthijain2005@gmail.com">Let's talk</a>
  </div>
</nav>

<main>
  <section class="hero">
    <div class="eyebrow"><span class="dot"></span> Open to 2026 software & program roles</div>
    <h1>I build systems<br>that <span>move.</span></h1>
    <p class="hero-copy">I'm Mishthi Jain, a computer science engineer turning complex systems into reliable, intuitive products. I work across backend infrastructure, real-time experiences, cloud systems, and cross-functional delivery.</p>
    <div class="actions">
      <a class="button primary" href="#work">Explore my work ↓</a>
      <a class="button secondary" href="https://github.com/MishthiJain8" target="_blank">GitHub ↗</a>
      <a class="button secondary" href="https://www.linkedin.com/in/mishthijain/" target="_blank">LinkedIn ↗</a>
    </div>
  </section>

  <section class="section">
    <div class="metrics">
      <div class="metric"><strong>559</strong><span>problems solved across coding platforms</span></div>
      <div class="metric"><strong>30+</strong><span>engineering projects built</span></div>
      <div class="metric"><strong>8.85</strong><span>CGPA in Computer Science</span></div>
      <div class="metric"><strong>2</strong><span>research manuscripts under review</span></div>
    </div>
  </section>

  <section class="section" id="experience">
    <div class="section-top">
      <div><div class="kicker">01 / Experience</div><h2>Built with teams.</h2></div>
      <p class="section-intro">Engineering is more than shipping code. I work across product, design, and infrastructure to turn ambiguous requirements into dependable experiences.</p>
    </div>
    <article class="experience">
      <div class="exp-head">
        <div><h3>Software Developer Intern · AyLark</h3><p>Platform & Systems Infrastructure · Nagpur, India</p></div>
        <span class="exp-date">DEC 2025 — MAR 2026</span>
      </div>
      <ul class="impact-list">
        <li>Developed full-stack features and microservices using TypeScript, Node.js, and PostgreSQL for collaborative productivity software.</li>
        <li>Implemented real-time synchronization with WebSockets and Redis, maintaining consistent state across connected clients.</li>
        <li>Partnered with designers and product managers, contributed to code reviews, and iterated on accessible, maintainable UI components.</li>
      </ul>
    </article>
  </section>

  <section class="section" id="work">
    <div class="section-top">
      <div><div class="kicker">02 / Selected work</div><h2>Ideas into impact.</h2></div>
      <p class="section-intro">A selection of systems shaped around performance, resilience, and the people using them.</p>
    </div>
    <div class="projects">
      <article class="project featured">
        <div class="project-number">Featured · Real-time systems</div>
        <h3>Discord-inspired communication platform</h3>
        <p>Designed a scalable real-time platform for chat, presence, and notifications, with consistent event delivery across clients.</p>
        <div class="tags"><span class="tag">TypeScript</span><span class="tag">Node.js</span><span class="tag">Redis Pub/Sub</span><span class="tag">PostgreSQL</span><span class="tag">WebSockets</span></div>
        <a class="project-link" href="https://github.com/MishthiJain8/Discord-inspired-real-time-communication-platform" target="_blank">View repository ↗</a>
      </article>
      <article class="project">
        <div class="project-number">Mobile product</div>
        <h3>Campus Connect</h3>
        <p>Built a cross-platform social and events app with chat, notifications, scheduling, and an offline-first experience.</p>
        <div class="tags"><span class="tag">React Native</span><span class="tag">TypeScript</span><span class="tag">Node.js</span></div>
        <a class="project-link" href="https://github.com/MishthiJain8/Campus-connect-mobile-app" target="_blank">View repository ↗</a>
      </article>
      <article class="project">
        <div class="project-number">Distributed systems</div>
        <h3>Real-time grocery platform</h3>
        <p>Engineered concurrent inventory and order synchronization with distributed caching for low-latency, resilient operations.</p>
        <div class="tags"><span class="tag">Java</span><span class="tag">Concurrency</span><span class="tag">Distributed Cache</span></div>
        <a class="project-link" href="https://github.com/MishthiJain8/real-time-grocery-platform" target="_blank">View repository ↗</a>
      </article>
      <article class="project">
        <div class="project-number">Cloud infrastructure</div>
        <h3>Cloud resource optimizer</h3>
        <p>Automated idle AWS resource detection and surfaced actionable utilization insights through an operations dashboard.</p>
        <div class="tags"><span class="tag">Python</span><span class="tag">AWS</span><span class="tag">Boto3</span><span class="tag">Automation</span></div>
        <a class="project-link" href="https://github.com/MishthiJain8" target="_blank">Explore GitHub ↗</a>
      </article>
      <article class="project">
        <div class="project-number">Developer education</div>
        <h3>Algorithm playground</h3>
        <p>Translated abstract sorting and graph algorithms into interactive, step-by-step visual flows for clearer learning.</p>
        <div class="tags"><span class="tag">Java</span><span class="tag">Algorithms</span><span class="tag">Visualization</span></div>
        <a class="project-link" href="https://github.com/MishthiJain8" target="_blank">Explore GitHub ↗</a>
      </article>
    </div>
  </section>

  <section class="section" id="research">
    <div class="section-top">
      <div><div class="kicker">03 / Research</div><h2>Curiosity, tested.</h2></div>
      <p class="section-intro">Applied machine learning research focused on making models more useful under real-world data and forecasting constraints.</p>
    </div>
    <div class="grid-3">
      <article class="card"><span class="card-label">Under review · CEECT 2026</span><h3>GAN-based synthetic augmentation</h3><p>Studying how synthetic data can improve deep-learning classifier generalization for Septoria detection in data-scarce environments.</p></article>
      <article class="card"><span class="card-label">Under review · Elsevier</span><h3>Soybean price forecasting</h3><p>A machine-learning approach to forecasting soybean prices in Maharashtra, submitted to Geoderma Regional.</p></article>
      <article class="card"><span class="card-label">Working style</span><h3>Evidence before assumption</h3><p>I enjoy defining measurable questions, testing systems under constraints, and communicating findings clearly across disciplines.</p></article>
    </div>
  </section>

  <section class="section" id="skills">
    <div class="section-top">
      <div><div class="kicker">04 / Capabilities</div><h2>Range with depth.</h2></div>
      <p class="section-intro">A broad technical base, anchored in backend engineering, distributed systems, and thoughtful product delivery.</p>
    </div>
    <div class="skills">
      <div class="skill-group"><h3>Languages</h3><p>C++ · Python · Java · TypeScript · SQL</p></div>
      <div class="skill-group"><h3>Backend engineering</h3><p>Spring Boot · Node.js · REST APIs · gRPC · Microservices</p></div>
      <div class="skill-group"><h3>Distributed systems</h3><p>Concurrency · Fault tolerance · Service discovery · Caching · Load balancing</p></div>
      <div class="skill-group"><h3>Cloud & infrastructure</h3><p>AWS · Docker · Kubernetes · CI/CD · Linux · Git</p></div>
      <div class="skill-group"><h3>Data & storage</h3><p>PostgreSQL · Redis · Relational modeling · ACID transactions</p></div>
      <div class="skill-group"><h3>Core computer science</h3><p>Data structures · Algorithms · Operating systems · Networks · OOP · System design</p></div>
    </div>
  </section>

  <section class="section" id="apple-fit">
    <div class="section-top">
      <div><div class="kicker">05 / Role alignment</div><h2>Ready to contribute.</h2></div>
      <p class="section-intro">My experience maps naturally to software engineering and engineering program management: hands-on building, systems thinking, and calm cross-functional execution.</p>
    </div>
    <div class="fit">
      <article class="fit-card"><span>SOFTWARE ENGINEERING</span><h3>Architecture to interface</h3><p>Experience across backend services, real-time data, mobile interfaces, testing, and performance-conscious implementation.</p></article>
      <article class="fit-card"><span>PROGRAM DELIVERY</span><h3>Complexity into plans</h3><p>Comfortable translating requirements, surfacing dependencies, coordinating with partners, and communicating technical tradeoffs.</p></article>
      <article class="fit-card"><span>PRODUCT MINDSET</span><h3>Useful, not just functional</h3><p>I care about accessibility, intuitive experiences, measurable outcomes, and the details that make technology feel effortless.</p></article>
    </div>
  </section>

  <footer class="footer">
    <div class="kicker">Let's build what comes next</div>
    <h2>Have an ambitious problem? I'm listening.</h2>
    <div class="actions">
      <a class="button primary" href="mailto:mishthijain2005@gmail.com">Email Mishthi ↗</a>
      <a class="button secondary" href="https://github.com/MishthiJain8" target="_blank">GitHub</a>
      <a class="button secondary" href="https://www.linkedin.com/in/mishthijain/" target="_blank">LinkedIn</a>
      <a class="button secondary" href="https://codolio.com/profile/MJ2005" target="_blank">Coding profile</a>
    </div>
    <div class="footer-bottom"><span>Mishthi Jain · Cupertino / Nagpur</span><span>Designed & engineered with intent · 2026</span></div>
  </footer>
</main>
""",
    unsafe_allow_html=True,
)
