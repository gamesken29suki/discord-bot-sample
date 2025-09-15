document.addEventListener("DOMContentLoaded", function() {
  const input = document.getElementById('commandSearch');
  input.addEventListener('input', function() {
    const filter = input.value.toLowerCase();
    // コマンド一覧テーブルのIDを「commands-table」に置き換えてください
    const rows = document.querySelectorAll('#commands-table tbody tr');
    rows.forEach(row => {
      row.style.display = row.textContent.toLowerCase().includes(filter) ? '' : 'none';
    });
  });
});
function filterCategory(cat) {
  const rows = document.querySelectorAll('#commands-table tbody tr');
  rows.forEach(row => {
    const category = row.cells[1].textContent.trim();
    if (cat === 'all' || category === cat) {
      row.style.display = '';
    } else {
      row.style.display = 'none';
    }
  });
  // ボタンのアクティブ切替（任意：Bootstrap用）
  document.querySelectorAll('.btn-outline-primary').forEach(btn => btn.classList.remove('active'));
  if(cat !== 'all') {
    document.querySelector(`button[onclick="filterCategory('${cat}')"]`).classList.add('active');
  }
}
const toggle = document.getElementById("darkModeToggle");
function updateButton() {
  toggle.textContent = document.body.classList.contains("dark-mode") ? "☀️ ライトモード" : "🌙 ダークモード";
}
toggle.addEventListener("click", function() {
  document.body.classList.toggle("dark-mode");
  localStorage.setItem("dark-mode", document.body.classList.contains("dark-mode") ? "on" : "off");
  updateButton();
});
// ページ読み込み時に保存した状態に復帰
if(localStorage.getItem("dark-mode") === "on") {
  document.body.classList.add("dark-mode");
}
updateButton();
window.addEventListener('DOMContentLoaded', function() {
  var toc = document.getElementById('toc');
  if (!toc) return;
  var headings = document.querySelectorAll('h2, h3');
  var list = document.createElement('ul');
  headings.forEach(function(heading, i) {
    if (!heading.id) heading.id = 'heading-' + i;
    var item = document.createElement('li');
    item.style.marginLeft = (heading.tagName === 'H3' ? '20px' : '0');
    item.innerHTML = '<a href="#' + heading.id + '">' + heading.textContent + '</a>';
