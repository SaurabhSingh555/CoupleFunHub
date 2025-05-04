document.addEventListener('DOMContentLoaded', function() {
    const spinBtn = document.getElementById('spin-btn');
    if (spinBtn) {
        spinBtn.addEventListener('click', function(e) {
            e.preventDefault();
            const spinner = document.querySelector('.spinner-wheel');
            if (spinner) {
                // Disable button during spin
                spinBtn.disabled = true;
                spinBtn.textContent = 'Spinning...';
                
                // Add spinning class
                spinner.classList.add('spinning');
                
                // After spinning completes
                setTimeout(function() {
                    // Submit the form
                    spinBtn.form.submit();
                }, 4000); // Match this with CSS transition duration
            }
        });
    }
});