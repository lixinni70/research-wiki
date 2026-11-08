// 研究 Wiki 網站：在瀏覽器端把 Markdown 轉成 HTML，並顯示數學式與 Obsidian callout。
(function () {
  const src = document.getElementById('md');
  const out = document.getElementById('content');
  if (!src || !out) return;
  let md = src.textContent;

  // 1) 先把數學式換成佔位符，避免 Markdown 解析器破壞 LaTeX
  const math = [];
  const keep = s => { math.push(s); return '@@MATH' + (math.length - 1) + '@@'; };
  // 不處理程式碼區塊與行內程式碼中的 $
  const parts = md.split(/(```[\s\S]*?```|`[^`\n]*`)/);
  md = parts.map((p, i) => i % 2 ? p :
    p.replace(/\$\$[\s\S]+?\$\$/g, keep).replace(/\$(?!\s)[^$\n]+?(?<!\s)\$/g, keep)
  ).join('');

  // 2) Markdown → HTML
  let html = marked.parse(md, { gfm: true, breaks: false });
  html = html.replace(/@@MATH(\d+)@@/g, (_, n) =>
    math[n].replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'));
  out.innerHTML = html;

  // 3) Obsidian callout：> [!warning] 標題
  out.querySelectorAll('blockquote').forEach(bq => {
    const p = bq.querySelector('p');
    if (!p) return;
    const m = p.innerHTML.match(/^\[!(\w+)\]\s*([^\n<]*)(?:<br>|\n)?/);
    if (!m) return;
    const type = m[1].toLowerCase();
    const names = { warning: '矛盾／注意', note: '備註', question: '待確認', info: '資訊' };
    const div = document.createElement('div');
    div.className = 'callout ' + type;
    p.innerHTML = p.innerHTML.slice(m[0].length);
    div.innerHTML = '<div class="ct">' + (m[2] || names[type] || type) + '</div>' + bq.innerHTML;
    bq.replaceWith(div);
  });

  // 4) 數學式
  if (window.renderMathInElement) {
    renderMathInElement(out, {
      delimiters: [{ left: '$$', right: '$$', display: true }, { left: '$', right: '$', display: false }],
      throwOnError: false
    });
  }
})();
