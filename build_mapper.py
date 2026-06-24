import pathlib
D = pathlib.Path('/Users/automattnick/Desktop/Claude Work/states')
def load(n): return D.joinpath(n+'.json').read_text()

# id -> source filename
FILES = [('reply_all','reply-all'),('reply_i1','reply_i1'),('reply_i2','reply_i2'),
         ('reply_i3','reply_i3'),('follow_i1','follow_i1'),('star_i1','star_i1')]
anim_data = ",\n".join(f'"{i}": {load(f)}' for i,f in FILES)

TEMPLATE = r'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Lottie segment mapper</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.12.2/lottie.min.js"></script>
<style>
  :root{--bd:#dcdcde;--ink:#3C434A;--blue:#0675c4;--font:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
  *{box-sizing:border-box}
  body{margin:0;padding:28px;font-family:var(--font);color:var(--ink);background:#eef0f1}
  h1{font-size:16px;margin:0 0 4px}
  p.sub{font-size:13px;color:#6b7177;margin:0 0 18px;line-height:1.5}
  .grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
  .card{background:#fff;border:1px solid var(--bd);border-radius:10px;padding:16px}
  .top{display:flex;gap:14px;align-items:flex-start}
  .preview{width:150px;height:150px;flex:0 0 150px;border:1px solid #eee;border-radius:8px;background:
    linear-gradient(45deg,#fafafa 25%,transparent 25%,transparent 75%,#fafafa 75%) 0 0/16px 16px,
    linear-gradient(45deg,#fafafa 25%,#fff 25%,#fff 75%,#fafafa 75%) 8px 8px/16px 16px;position:relative;overflow:hidden}
  .preview .lottie{position:absolute;inset:0}
  .meta{flex:1;min-width:0}
  .name{font-size:14px;font-weight:600;margin-bottom:8px}
  .modeRow{font-size:12px;display:flex;gap:14px;margin-bottom:10px}
  .modeRow label{display:inline-flex;gap:4px;align-items:center;cursor:pointer}
  .btn{font:inherit;font-size:12px;padding:5px 10px;border:1px solid var(--bd);border-radius:6px;background:#fff;cursor:pointer}
  .btn:hover{background:#f6f7f7}
  .scrub{width:100%;margin:12px 0 4px}
  .frameRow{display:flex;justify-content:space-between;font-size:12px;color:#555;font-variant-numeric:tabular-nums;margin-bottom:10px}
  .frameRow .frame b{color:#111}
  .states{display:flex;flex-direction:column;gap:7px}
  .srow{display:flex;align-items:center;gap:8px;font-size:12px;flex-wrap:wrap}
  .slabel{flex:0 0 168px;color:#3c434a}
  .srow input[type=number]{width:54px;font:inherit;font-size:12px;padding:3px 5px;border:1px solid var(--bd);border-radius:5px;text-align:right}
  .srow .mini{font:inherit;font-size:11px;padding:3px 6px;border:1px solid var(--bd);border-radius:5px;background:#fff;cursor:pointer}
  .srow .mini:hover{background:#eef5fb;border-color:#bcd}
  .srow .play{border:none;background:none;color:var(--blue);cursor:pointer;font-size:13px;padding:2px 4px}
  .srow .k{color:#9aa0a6}
  .cardfoot{margin-top:12px;display:flex;gap:8px}
  .exportbar{margin:20px 0 8px;display:flex;gap:10px;align-items:center}
  textarea{width:100%;height:200px;font:12px/1.4 ui-monospace,Menlo,monospace;border:1px solid var(--bd);border-radius:8px;padding:10px;margin-top:8px}
</style></head>
<body>
<h1>Lottie segment mapper</h1>
<p class="sub">Scrub each animation, watch the <b>frame</b> readout, and click <b>⇐ set</b> / <b>set ⇒</b> to capture the current frame as a state's start/end. Frames shown are <b>absolute comp frames</b> (what playSegments uses). <b>▶</b> on a row previews that segment. Toggle <b>Hover only</b> for files with just hover on/off. Then <b>Export</b> and paste the result back to me.</p>

<div class="grid" id="grid"></div>

<div class="exportbar">
  <button class="btn" id="exportBtn">⤓ Export all segments</button>
  <button class="btn" id="copyBtn">Copy to clipboard</button>
  <span id="copyMsg" style="font-size:12px;color:#0a7c2f"></span>
</div>
<textarea id="out" readonly placeholder="Exported JSON appears here…"></textarea>

<script>
const ANIM_DATA = {
__ANIM_DATA__
};
const FILES = [
  {id:'reply_all', label:'reply-all', mode:'full'},
  {id:'reply_i1',  label:'reply_i1',  mode:'hover'},
  {id:'reply_i2',  label:'reply_i2',  mode:'hover'},
  {id:'reply_i3',  label:'reply_i3',  mode:'hover'},
  {id:'follow_i1', label:'follow_i1', mode:'full'},
  {id:'star_i1',   label:'star_i1',   mode:'full'},
];
const VIEWBOX = { reply_all:'60 128 100 100', reply_i1:'78 86 100 100', reply_i2:'82 82 100 100',
                  reply_i3:'85 81 100 100', follow_i1:'103 83 100 100', star_i1:'123 100 100 100' };
// starting guesses (absolute comp frames) - adjust freely
const PREFILL = {
  reply_all:{hoverOnInactive:[19,58],clickInactive:[67,98],hoverOffInactive:[216,237],hoverOnActive:[138,166],clickActive:[184,214],hoverOffActive:[106,129]},
  reply_i1:{hoverOn:[16,117]}, reply_i2:{hoverOn:[16,117]}, reply_i3:{hoverOn:[15,116]},
  follow_i1:{hoverOnInactive:[54,62],clickInactive:[82,113],hoverOffInactive:[164,166],clickActive:[144,163]},
  star_i1:{hoverOnInactive:[22,74],clickInactive:[92,135],hoverOffInactive:[160,164],clickActive:[138,159]},
};
const FULL_STATES = [
  ['hoverOnInactive','hover-on · NOT active'], ['clickInactive','click · NOT active'], ['hoverOffInactive','hover-off · NOT active'],
  ['hoverOnActive','hover-on · active'], ['clickActive','click · active'], ['hoverOffActive','hover-off · active'],
];
const HOVER_STATES = [ ['hoverOn','hover-on'], ['hoverOff','hover-off'] ];

const $ = (s,r=document)=>r.querySelector(s);
const STORE = {};   // id -> { key:[s,e] }
const ANIMS = {};   // id -> { anim, ip, op, scrub, frameEl, playing }

function makeCard(cfg){
  STORE[cfg.id] = Object.assign({}, JSON.parse(JSON.stringify(PREFILL[cfg.id]||{})));
  const card = document.createElement('div'); card.className='card'; card.dataset.id=cfg.id;
  card.innerHTML = `
    <div class="top">
      <div class="preview"><div class="lottie" id="lot-${cfg.id}"></div></div>
      <div class="meta">
        <div class="name">${cfg.label}</div>
        <div class="modeRow">
          <label><input type="radio" name="mode-${cfg.id}" value="full" ${cfg.mode==='full'?'checked':''}> Full (6 states)</label>
          <label><input type="radio" name="mode-${cfg.id}" value="hover" ${cfg.mode==='hover'?'checked':''}> Hover only (2)</label>
        </div>
        <button class="btn playFull">▶ play 0–100%</button>
      </div>
    </div>
    <input type="range" class="scrub" min="0" max="100" value="0">
    <div class="frameRow"><span class="frame">frame <b>–</b> / –</span><span class="rng"></span></div>
    <div class="states"></div>`;
  $('#grid').appendChild(card);

  const anim = lottie.loadAnimation({ container:$('#lot-'+cfg.id), renderer:'svg', loop:false, autoplay:false, animationData:ANIM_DATA[cfg.id] });
  const rec = ANIMS[cfg.id] = { anim, ip:0, op:1, playing:false };
  const scrub = $('.scrub', card), frameEl = $('.frame', card), rngEl = $('.rng', card);
  rec.scrub = scrub; rec.frameEl = frameEl;

  const setFrameLabel = abs => {
    const pct = rec.op>rec.ip ? Math.round((abs-rec.ip)/(rec.op-rec.ip)*100) : 0;
    frameEl.innerHTML = `frame <b>${abs}</b> / ${rec.op} &nbsp;(${pct}%)`;
  };
  const goAbs = abs => anim.goToAndStop(abs - anim.firstFrame, true);  // firstFrame, not ip — playSegments() moves the base

  anim.addEventListener('DOMLoaded', ()=>{
    rec.ip = Math.round(anim.firstFrame);
    rec.op = Math.round(anim.firstFrame + anim.totalFrames);
    const svg = anim.renderer && anim.renderer.svgElement;
    if(svg && VIEWBOX[cfg.id]){ svg.setAttribute('viewBox', VIEWBOX[cfg.id]); svg.setAttribute('preserveAspectRatio','xMidYMid meet'); }
    scrub.min = rec.ip; scrub.max = rec.op; scrub.value = rec.ip;
    rngEl.textContent = `ip ${rec.ip} · op ${rec.op} · ${anim.frameRate}fps`;
    goAbs(rec.ip); setFrameLabel(rec.ip);
    buildStates(cfg.id, cfg.mode);
  });

  anim.addEventListener('enterFrame', ()=>{
    if(!rec.playing) return;
    const abs = Math.round(anim.firstFrame + anim.currentFrame);
    scrub.value = abs; setFrameLabel(abs);
  });
  anim.addEventListener('complete', ()=>{ rec.playing=false; $('.playFull',card).textContent='▶ play 0–100%'; });

  scrub.addEventListener('input', ()=>{ pause(cfg.id); const abs=+scrub.value; goAbs(abs); setFrameLabel(abs); });

  $('.playFull',card).addEventListener('click', e=>{
    if(rec.playing){ pause(cfg.id); } else { anim.loop=true; rec.playing=true; anim.playSegments([rec.ip,rec.op],true); e.target.textContent='⏸ pause'; }
  });
  card.querySelectorAll(`input[name="mode-${cfg.id}"]`).forEach(r=>r.addEventListener('change',e=>buildStates(cfg.id,e.target.value)));
  return rec;
}

function pause(id){ const r=ANIMS[id]; if(!r) return; r.anim.loop=false; r.anim.pause(); r.playing=false;
  const c=document.querySelector(`.card[data-id="${id}"] .playFull`); if(c) c.textContent='▶ play 0–100%'; }

function buildStates(id, mode){
  const card = document.querySelector(`.card[data-id="${id}"]`);
  const host = $('.states', card); host.innerHTML='';
  const states = mode==='hover' ? HOVER_STATES : FULL_STATES;
  states.forEach(([key,label])=>{
    const v = (STORE[id][key]||[]);
    const row = document.createElement('div'); row.className='srow'; row.dataset.key=key;
    row.innerHTML = `<span class="slabel">${label}</span>
      <span class="k">start</span><input class="s" type="number" value="${v[0]??''}">
      <button class="mini setS">⇐ set</button>
      <span class="k">end</span><input class="e" type="number" value="${v[1]??''}">
      <button class="mini setE">set ⇒</button>
      <button class="play" title="preview segment">▶</button>`;
    host.appendChild(row);
    const sIn=$('.s',row), eIn=$('.e',row), rec=ANIMS[id];
    const save=()=>{ STORE[id][key]=[sIn.value===''?null:+sIn.value, eIn.value===''?null:+eIn.value]; };
    sIn.addEventListener('input',save); eIn.addEventListener('input',save);
    $('.setS',row).addEventListener('click',()=>{ sIn.value=Math.round(+rec.scrub.value); save(); });
    $('.setE',row).addEventListener('click',()=>{ eIn.value=Math.round(+rec.scrub.value); save(); });
    $('.play',row).addEventListener('click',()=>{
      const s=+sIn.value, e=+eIn.value; if(isNaN(s)||isNaN(e)) return;
      pause(id); rec.anim.loop=false; rec.playing=true; rec.anim.playSegments([Math.min(s,e),Math.max(s,e)],true);
    });
  });
}

FILES.forEach(makeCard);

function buildExport(){
  const out={};
  FILES.forEach(f=>{
    const mode = document.querySelector(`input[name="mode-${f.id}"]:checked`).value;
    const keys = (mode==='hover'?HOVER_STATES:FULL_STATES).map(s=>s[0]);
    const segs={}; keys.forEach(k=>{ const v=STORE[f.id][k]; if(v && v[0]!=null && v[1]!=null) segs[k]=[Math.min(v[0],v[1]),Math.max(v[0],v[1])]; });
    out[f.id]={ mode, ip:ANIMS[f.id].ip, op:ANIMS[f.id].op, segments:segs };
  });
  return JSON.stringify(out,null,2);
}
$('#exportBtn').addEventListener('click',()=>{ $('#out').value=buildExport(); });
$('#copyBtn').addEventListener('click',async()=>{ const t=buildExport(); $('#out').value=t;
  try{ await navigator.clipboard.writeText(t); $('#copyMsg').textContent='copied ✓'; setTimeout(()=>$('#copyMsg').textContent='',1500);}catch(e){ $('#copyMsg').textContent='select & copy from box below'; } });
</script>
</body></html>'''

out = pathlib.Path('/Users/automattnick/Desktop/Claude Work/segment-mapper.html')
out.write_text(TEMPLATE.replace('__ANIM_DATA__', anim_data))
print('written', out.stat().st_size, 'bytes')
