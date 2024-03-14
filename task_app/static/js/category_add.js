function handleCategoryChange() {
    var categorySelect = document.getElementById("id_category");
    var otherCategoryInput = document.getElementById("other-category");

    categorySelect.addEventListener("change", function() {
        if (categorySelect.value === "Other") {
            otherCategoryInput.style.display = "block";
            otherCategoryInput.setAttribute("name", "other_category");
        } else {
            otherCategoryInput.style.display = "none";
            otherCategoryInput.removeAttribute("name");
        }
    });
}

document.addEventListener("DOMContentLoaded", handleCategoryChange);
