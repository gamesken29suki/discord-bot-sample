// ダークモード切り替え
const toggle = document.getElementById("darkModeToggle");
function updateButton() {
  toggle.textContent = document.body.classList.contains("dark-mode") ? "☀️ ライトモード" : "🌙 ダークモード";
}
toggle.addEventListener("click", function() {
  document.body.classList.toggle("dark-mode");
  localStorage.setItem("dark-mode", document.body.classList.contains("dark-mode") ? "on" : "off");
  updateButton();
});
if(localStorage.getItem("dark-mode") === "on") {
  document.body.classList.add("dark-mode");
}
updateButton();

// コマンド検索・カテゴリフィルタ（必要なら同じファイル内に記述）
function filterCategory(cat) {
  const rows = document.querySelectorAll('#commands-table tbody tr');
  rows.forEach(row => {
    const category = row.cells[1].textContent.trim();
    row.style.display = (cat === 'all' || category === cat) ? '' : 'none';
  });
}
document.addEventListener("DOMContentLoaded", function() {
  const input = document.getElementById('commandSearch');
  if(input){
    input.addEventListener('input', function() {
      const filter = input.value.toLowerCase();
      const rows = document.querySelectorAll('#commands-table tbody tr');
      rows.forEach(row => {
        row.style.display = row.textContent.toLowerCase().includes(filter) ? '' : 'none';
      });
    });
  }
});
