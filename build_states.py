import json, pathlib

D = pathlib.Path('/Users/automattnick/Desktop/Claude Work/states')
def load(n): return D.joinpath(n+'.json').read_text()

REPLY_TEXT = "M66.2979 41V22.6807H73.5215C77.2793 24.8643 79.6152 24.8643 79.6152 28.2666V28.292C79.6152 30.7549 78.2949 32.7607 76.0605 33.5098L80.1738 41H76.8857L73.1533 33.9541H69.1416V41H66.2979ZM69.1416 31.6436H73.2422C75.4258 31.6436 76.6953 30.4502 76.6953 28.3682V28.3428C76.6953 26.3115 75.3496 25.0674 73.1533 25.0674H69.1416V31.6436ZM88.7305 41.2666C84.6934 41.2666 82.2559 38.5117 82.2559 34.1445V34.1318C82.2559 29.8281 84.7441 26.9463 88.5908 26.9463C92.4375 26.9463 94.7988 29.7266 94.7988 33.8652V34.8301H85.0234C85.0742 37.4707 86.5215 39.0068 88.7939 39.0068C90.5586 39.0068 91.6123 38.1309 91.9424 37.4199L91.9932 37.3184L94.6465 37.3057L94.6211 37.4199C94.1641 39.2354 92.2598 41.2666 88.7305 41.2666ZM88.6035 29.2061C86.7246 29.2061 85.3027 30.4883 85.0615 32.8623H92.0693C91.8535 30.3994 90.4697 29.2061 88.6035 29.2061ZM98.0742 45.5957V27.2129H100.829V29.3838H101.032C101.832 27.873 103.343 26.9717 105.272 26.9717C108.751 26.9717 110.985 29.752 110.985 34.0938V34.1191C110.985 38.4863 108.776 41.2285 105.272 41.2285C103.381 41.2285 101.769 40.3018 101.032 38.8164H100.829V45.5957H98.0742ZM104.498 38.8799C106.796 38.8799 108.18 37.0771 108.18 34.1191V34.0938C108.18 31.123 106.796 29.333 104.498 29.333C102.2 29.333 100.778 31.1484 100.778 34.0938V34.1191C100.778 37.0645 102.2 38.8799 104.498 38.8799ZM114.426 41V21.8047H117.181V41H114.426ZM122.627 45.8496C122.284 45.8496 121.878 45.8242 121.522 45.7861V43.6152C121.789 43.6533 122.132 43.666 122.449 43.666C123.731 43.666 124.493 43.1201 124.912 41.7236L125.115 41.0127L120.113 27.2129H123.084L126.537 38.2324H126.778L130.219 27.2129H133.113L127.984 41.5332C126.816 44.834 125.42 45.8496 122.627 45.8496Z"
FOLLOW_TEXT = "M62.2979 41.5V23.1807H73.7363V25.6309H65.1416V31.4326H73.0127V33.832H65.1416V41.5H62.2979ZM82.9531 41.7666C78.9033 41.7666 76.4277 39.0625 76.4277 34.6191V34.5938C76.4277 30.1631 78.916 27.4463 82.9531 27.4463C86.9775 27.4463 89.4658 30.1504 89.4658 34.5938V34.6191C89.4658 39.0625 86.9902 41.7666 82.9531 41.7666ZM82.9531 39.4688C85.3145 39.4688 86.6602 37.666 86.6602 34.6191V34.5938C86.6602 31.5342 85.3145 29.7441 82.9531 29.7441C80.5791 29.7441 79.2461 31.5342 79.2461 34.5938V34.6191C79.2461 37.6787 80.5791 39.4688 82.9531 39.4688ZM92.8809 41.5V22.3047H95.6357V41.5H92.8809ZM99.8633 41.5V22.3047H102.618V41.5H99.8633ZM112.559 41.7666C108.509 41.7666 106.033 39.0625 106.033 34.6191V34.5938C106.033 30.1631 108.521 27.4463 112.559 27.4463C116.583 27.4463 119.071 30.1504 119.071 34.5938V34.6191C119.071 39.0625 116.596 41.7666 112.559 41.7666ZM112.559 39.4688C114.92 39.4688 116.266 37.666 116.266 34.6191V34.5938C116.266 31.5342 114.92 29.7441 112.559 29.7441C110.185 29.7441 108.852 31.5342 108.852 34.5938V34.6191C108.852 37.6787 110.185 39.4688 112.559 39.4688ZM124.479 41.5L120.671 27.7129H123.438L125.914 38.3516H126.117L128.961 27.7129H131.576L134.42 38.3516H134.636L137.099 27.7129H139.828L136.032 41.5H133.201L130.345 31.2168H130.129L127.285 41.5H124.479Z"
LIKE_TEXT = "M64.2979 41.5V23.1807H67.1416V39.0498H75.7236V41.5H64.2979ZM80.4463 25.25C79.4941 25.25 78.7197 24.4756 78.7197 23.5361C78.7197 22.584 79.4941 21.8096 80.4463 21.8096C81.3857 21.8096 82.1729 22.584 82.1729 23.5361C82.1729 24.4756 81.3857 25.25 80.4463 25.25ZM79.0625 41.5V27.7129H81.8047V41.5H79.0625ZM85.9434 41.5V22.3047H88.6982V33.5273H88.9014L94.373 27.7129H97.5977L91.8467 33.5273L97.9785 41.5H94.627L89.8789 35.3047L88.6982 36.4854V41.5H85.9434ZM105.57 41.7666C101.533 41.7666 99.0957 39.0117 99.0957 34.6445V34.6318C99.0957 30.3281 101.584 27.4463 105.431 27.4463C109.277 27.4463 111.639 30.2266 111.639 34.3652V35.3301H101.863C101.914 37.9707 103.361 39.5068 105.634 39.5068C107.398 39.5068 108.452 38.6309 108.782 37.9199L108.833 37.8184L111.486 37.8057L111.461 37.9199C111.004 39.7354 109.1 41.7666 105.57 41.7666ZM105.443 29.7061C103.564 29.7061 102.143 30.9883 101.901 33.3623H108.909C108.693 30.8994 107.31 29.7061 105.443 29.7061Z"

# button geometry per type: (svg width, text path, icon overlay style)
TYPES = {
  'reply':  (182, REPLY_TEXT, "left:13px; top:17px; width:44px; height:30px;"),
  'follow': (165, FOLLOW_TEXT, "left:15px; top:14px; width:36px; height:36px;"),
  'star':   (137, LIKE_TEXT,   "left:5px;  top:2px;  width:58px; height:58px;"),
}

def btn_svg(t):
    w, text, _ = TYPES[t]
    inner = w-2
    return (f'<svg width="{w}" height="64" viewBox="0 0 {w} 64" fill="none" xmlns="http://www.w3.org/2000/svg">'
            f'<rect class="box" x="1" y="1" width="{inner}" height="62" rx="7" fill="white"/>'
            f'<rect x="1" y="1" width="{inner}" height="62" rx="7" stroke="#DCDCDE" stroke-width="2"/>'
            f'<path d="{text}" fill="#3C434A"/></svg>')

# per-button config: id, type, file, label, viewBox, hoverOnly, segments(abs), holds(abs)
BUTTONS = [
 dict(id='reply_i1', type='reply', file='reply_i1', label='reply_i1 (hover)',
      viewBox='90 113 75 45', ico='left:12px; top:16px; width:46px; height:31px;', hoverOnly=True,
      seg=dict(hoverOn=[43,74], hoverOff=[84,89]),
      hold=dict(idleUnpressed=16, afterHoverOn=74, afterHoverOff=89)),
 dict(id='reply_i2', type='reply', file='reply_i2', label='reply_i2 (hover)',
      viewBox='110 114 47 37', ico='left:15px; top:18px; width:40px; height:28px;', hoverOnly=True,
      seg=dict(hoverOn=[44,79], hoverOff=[84,109]),
      hold=dict(idleUnpressed=16, afterHoverOn=79, afterHoverOff=109)),
 dict(id='reply_i3', type='reply', file='reply_i3', label='reply_i3 (hover)',
      viewBox='110 113 50 39', ico='left:12px; top:16px; width:46px; height:31px;', hoverOnly=True,
      seg=dict(hoverOn=[40,64], hoverOff=[84,105]),
      hold=dict(idleUnpressed=15, afterHoverOn=64, afterHoverOff=105)),
 dict(id='follow_i1', type='follow', file='follow_i1', label='follow_i1 (toggle)',
      viewBox='123.6 103.7 58 58', ico='left:13px; top:12px; width:40px; height:40px;', hoverOnly=False,
      seg=dict(hoverOnUnpressed=[54,62], pressFromUnpressed=[82,113], hoverOffWhilePressed=[116,117],
               hoverOnWhilePressed=[118,120], pressWhilePressed=[144,163], hoverOffUnpressed=[164,166]),
      hold=dict(idleUnpressed=40, afterHoverOnUnpressed=62, afterPress=113, afterHoverOffWhilePressed=117,
                afterHoverOnWhilePressed=120, afterUnpress=163, afterHoverOffUnpressed=166)),
 dict(id='star_i1', type='star', file='star_i1', label='star_i1 (toggle)',
      viewBox='147 125 52 52', ico='left:14px; top:11px; width:41px; height:41px;', hoverOnly=False,
      seg=dict(hoverOnUnpressed=[18,80], pressFromUnpressed=[92,129], hoverOffWhilePressed=[127,128],
               hoverOnWhilePressed=[129,130], pressWhilePressed=[138,159], hoverOffUnpressed=[160,164]),
      hold=dict(idleUnpressed=0, afterHoverOnUnpressed=80, afterPress=129, afterHoverOffWhilePressed=128,
                afterHoverOnWhilePressed=130, afterUnpress=159, afterHoverOffUnpressed=164)),
]

def btn_html(b):
    icostyle = b.get('ico') or TYPES[b['type']][2]
    return (f'<button class="exact-btn" id="btn-{b["id"]}" type="button">'
            f'{btn_svg(b["type"])}<span class="ico" id="ico-{b["id"]}" style="{icostyle}"></span></button>')

by_id = {b['id']: b for b in BUTTONS}
top_row  = "".join(btn_html(by_id[i]) for i in ['reply_i1','follow_i1','star_i1'])
col_rows = "".join(f'<div class="frow">{btn_html(by_id[i])}</div>' for i in ['reply_i2','reply_i3'])

# JS config + anim data
anim_js = ",\n".join(f'"{b["id"]}": {load(b["file"])}' for b in BUTTONS)
def cfg_one(b):
    return json.dumps({'viewBox': b['viewBox'], 'hoverOnly': b['hoverOnly'], 'seg': b['seg'], 'hold': b['hold']})
cfg_js = ",\n".join(f'"{b["id"]}": {cfg_one(b)}' for b in BUTTONS)

HTML = f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>O2 stateful buttons</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.12.2/lottie.min.js"></script>
<style>
  :root{{ --o2-border:#DCDCDE; --o2-link:#0675c4; --o2-font:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif; }}
  *{{box-sizing:border-box}}
  body{{margin:0;min-height:100vh;font-family:var(--o2-font);color:#3C434A;background:#e7e9ec;-webkit-font-smoothing:antialiased}}
  .backdrop{{position:fixed;inset:0;background:rgba(15,20,28,.5);display:flex;align-items:center;justify-content:center;padding:24px;transition:opacity .22s ease}}
  .backdrop.hidden{{opacity:0;pointer-events:none}}
  .modal{{position:relative;background:#fff;border-radius:16px;box-shadow:0 24px 64px rgba(8,12,20,.30),0 3px 10px rgba(8,12,20,.10);padding:30px 38px 34px;transition:transform .22s cubic-bezier(.2,.8,.25,1),opacity .22s ease}}
  .backdrop.hidden .modal{{transform:scale(.96) translateY(6px);opacity:0}}
  .modal-close{{position:absolute;top:13px;right:13px;width:30px;height:30px;display:flex;align-items:center;justify-content:center;border:none;background:none;border-radius:8px;color:#9aa0a6;cursor:pointer;transition:background .12s,color .12s}}
  .modal-close:hover{{background:#f1f2f4;color:#3c434a}}
  .modal-close svg{{width:15px;height:15px}}
  .stack{{display:flex;flex-direction:column;gap:18px;align-items:flex-start;zoom:0.82}}
  .frow{{display:flex;gap:18px;align-items:center}}
  .trigger{{position:fixed;left:24px;top:24px;font:inherit;font-size:14px;padding:9px 15px;border:1px solid #d4d6da;border-radius:9px;background:#fff;color:#3c434a;cursor:pointer;box-shadow:0 1px 2px rgba(0,0,0,.06)}}
  .trigger:hover{{background:#f7f8f9}}
  .trigger.hidden{{display:none}}
  .exact-btn{{position:relative;display:block;padding:0;border:none;background:none;cursor:pointer;-webkit-tap-highlight-color:transparent;transition:transform .09s ease}}
  .exact-btn>svg{{display:block}}
  .exact-btn .box{{transition:fill .15s ease}}
  .exact-btn:hover .box{{fill:#f6f7f7}}
  .exact-btn:active{{transform:scale(0.96)}}
  .exact-btn:active .box{{fill:#eef0f1}}
  .divider{{align-self:stretch;height:1px;background:#e6e7e9;margin:2px 0}}
  .ico{{position:absolute;pointer-events:none}}
  .ico svg{{width:100%;height:100%;display:block;overflow:visible}}
</style></head>
<body>
<div class="backdrop" id="backdrop">
  <div class="modal" role="dialog" aria-modal="true" aria-label="Post reactions">
    <button class="modal-close" id="closeModal" type="button" aria-label="Close">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
    <div class="stack">
      <div class="frow">{top_row}</div>
      <div class="divider"></div>
      {col_rows}
    </div>
  </div>
</div>
<button class="trigger hidden" id="openModal" type="button">Open dialog</button>
<script>
const ANIM_DATA = {{
{anim_js}
}};
const CFG = {{
{cfg_js}
}};
const $ = s => document.querySelector(s);

function wire(id){{
  const data = ANIM_DATA[id], cfg = CFG[id];
  const slot = $('#ico-'+id);
  const anim = lottie.loadAnimation({{container:slot, renderer:'svg', loop:false, autoplay:false, animationData:data}});
  const ip = data.ip || 0;
  let pressed = false, holdAbs = cfg.hold.idleUnpressed;
  // goToAndStop is relative to the CURRENT firstFrame, which playSegments() changes to the
  // segment start. So to land on absolute comp frame `abs`, subtract the live firstFrame.
  const rest = abs => anim.goToAndStop(abs - anim.firstFrame, true);
  anim.addEventListener('DOMLoaded', ()=>{{
    const svg = anim.renderer && anim.renderer.svgElement;
    if(svg && cfg.viewBox){{ svg.setAttribute('viewBox', cfg.viewBox); svg.setAttribute('preserveAspectRatio','xMidYMid meet'); }}
    rest(cfg.hold.idleUnpressed);
  }});
  anim.addEventListener('complete', ()=> rest(holdAbs));   // pin segment-end frame
  const play = (seg, hold)=>{{ if(!seg) return; holdAbs = hold; anim.playSegments(seg, true); }};  // playSegments is absolute
  const btn = $('#btn-'+id);
  btn.addEventListener('mouseenter', ()=>{{
    if(cfg.hoverOnly){{ play(cfg.seg.hoverOn, cfg.hold.afterHoverOn); return; }}
    if(pressed) play(cfg.seg.hoverOnWhilePressed, cfg.hold.afterHoverOnWhilePressed);
    else        play(cfg.seg.hoverOnUnpressed,    cfg.hold.afterHoverOnUnpressed);
  }});
  btn.addEventListener('mouseleave', ()=>{{
    if(cfg.hoverOnly){{ play(cfg.seg.hoverOff, cfg.hold.afterHoverOff); return; }}
    if(pressed) play(cfg.seg.hoverOffWhilePressed, cfg.hold.afterHoverOffWhilePressed);
    else        play(cfg.seg.hoverOffUnpressed,    cfg.hold.afterHoverOffUnpressed);
  }});
  btn.addEventListener('click', ()=>{{
    if(cfg.hoverOnly) return;
    if(pressed){{ pressed=false; play(cfg.seg.pressWhilePressed, cfg.hold.afterUnpress); }}
    else       {{ pressed=true;  play(cfg.seg.pressFromUnpressed, cfg.hold.afterPress); }}
  }});
  return anim;
}}
window.ANIMS = {{}};
Object.keys(CFG).forEach(id => window.ANIMS[id] = wire(id));

/* modal open / close */
(function(){{
  const bd=$('#backdrop'), openBtn=$('#openModal'), closeBtn=$('#closeModal');
  const hide=()=>{{ bd.classList.add('hidden'); openBtn.classList.remove('hidden'); }};
  const show=()=>{{ bd.classList.remove('hidden'); openBtn.classList.add('hidden'); }};
  closeBtn.addEventListener('click', hide);
  openBtn.addEventListener('click', show);
  bd.addEventListener('mousedown', e=>{{ if(e.target===bd) hide(); }});
  document.addEventListener('keydown', e=>{{ if(e.key==='Escape' && !bd.classList.contains('hidden')) hide(); }});
}})();
</script></body></html>'''

out = pathlib.Path('/Users/automattnick/Desktop/Claude Work/states-buttons.html')
out.write_text(HTML)
print('written', len(HTML), 'bytes to', out)
