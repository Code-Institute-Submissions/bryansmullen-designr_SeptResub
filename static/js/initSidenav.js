/**
 * initializes sidenav
 */
 const initialize = () => {
    const elems = document.querySelectorAll('.sidenav');
    M.Sidenav.init(elems);
};

// listener
document.addEventListener('DOMContentLoaded', initialize);