
const API_TOKEN = 'SecretToken123'
// FUnction to create elements
function makeEmotionElements() {
    const container = document.getElementById('emotionsContainer');
    container.innerHTML = '';
    
    // Emociones iniciales con valor 0
    const emotions = [
        { name: 'joy', value: 0 },
        { name: 'sadness', value: 0 },
        { name: 'anger', value: 0 },
        { name: 'fear', value: 0 },
        { name: 'surprise', value: 0 },
        { name: 'neutral', value: 0 }
    ];
    
    // Make a progress bar for every emotion
    emotions.forEach(emotion => {
        const emotionBar = document.createElement('div');
        emotionBar.className = 'emotion-bar';
        
        // HTML structure for every emotion
        emotionBar.innerHTML = `
            <div class="emotion-label">
                <span class="emotion-name ${emotion.name}">${emotion.name}</span>
                <span class="emotion-value ${emotion.name}">${emotion.value}%</span>
            </div>
            <div class="progress-container">
                <div class="progress-fill" id=bar-${emotion.name} data-value="${emotion.value}"></div>
            </div>
        `;
        
        container.appendChild(emotionBar);
    });
}

// Function to update the percentage for each bar
function updateEmotions(emotionsData) {
    const emotionBars = document.querySelectorAll('.emotion-bar');
    
    // Update bar
    emotionBars.forEach(bar => {
        const emotionName = bar.querySelector('.emotion-name').textContent;
        const emotionValue = bar.querySelector('.emotion-value');
        const progressFill = bar.querySelector('.progress-fill');
        
        // Get emotion value
        const targetValue = (emotionsData[emotionName]*100).toFixed(2);
        animateValue(emotionValue, 0, targetValue, 1500);
        animateProgressBar(progressFill, 0, targetValue, 1500);
        
    });
}

// Function to animate de value
function animateValue(element, start, end, duration) {
    const startTime = performance.now();
    const change = end - start;
    
    function updateValue(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1); // Normalizer (0-1)
        
        // Easing animation
        const easeOutQuart = 1 - Math.pow(1 - progress, 4);
        const currentValue = Math.floor(start + change * easeOutQuart);
        
        element.textContent = `${currentValue}%`;
        
        // Continue if isnt over
        if (progress < 1) {
            requestAnimationFrame(updateValue);
        } else {
            element.textContent = `${end}%`; // final value
        }
    }
    
    requestAnimationFrame(updateValue);
}

// Function to animate progress bar
function animateProgressBar(element, start, end, duration) {
    const startTime = performance.now();
    const change = end - start;
    
    function updateProgress(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Easing animation
        const easeOutQuart = 1 - Math.pow(1 - progress, 4);
        const currentValue = start + change * easeOutQuart;
        
        element.style.width = `${currentValue}%`;
        
        // Continue if isnt over
        if (progress < 1) {
            requestAnimationFrame(updateProgress);
        } else {
            element.style.width = `${end}%`; // final
        }
    }
    
    requestAnimationFrame(updateProgress);
}

// Update topics
function updateTopics(topicsData) {
    const topicsList = document.getElementById('topicsList');
    topicsList.innerHTML = ''; // Clean list
    
    // is there topics to show?
    if (topicsData && topicsData.length > 0) {
        // make a for every topic
        topicsData.forEach(topic => {
            const li = document.createElement('a');
            li.textContent = topic;
            topicsList.appendChild(li);
        });
    } else {
        // Show if there is no topics
        const li = document.createElement('a');
        li.textContent = 'No se detectaron tópicos';
        topicsList.appendChild(li);
    }
}

// Event listener for analysis
document.getElementById('analyseBtn').addEventListener('click', async ()=>{
    const btn = document.getElementById('analyseBtn');
    const spinner = document.getElementById('spinner');
    const mail = document.getElementById('mailInput').value.trim();
    
    // Valid textArea
    if(!mail){ 
        alert('Please paste a e-mail'); 
        return; 
    }

    // Deactivate buton and show spiner
    btn.disabled=true; 
    spinner.style.display='inline';
    makeEmotionElements(); // Make 0 every bar

    try{
        
        //api callhttps://witema.onrender.com/
        const resp = await fetch('https://witema.onrender.com/api/analyse/', {
            method:'POST',
            headers:{ 
                'Content-Type':'application/json',
                'Authorization':'Token '+API_TOKEN 
            },
            body: JSON.stringify({mail})
        });
        
        const data = await resp.json();
        
        // Answer?
        if(!resp.ok){ 
            alert(data.error||'Error del servidor'); 
            return; 
        }
        //console.log(data)
        // Update values
        updateEmotions(data.emotions);
        updateTopics(data.topics);
        
        
    }catch(err){ 
        console.error(err); 
        alert('Error de conexión'); 
    }
    finally{ 
        // Reset values
        btn.disabled=false; 
        spinner.style.display='none'; 
    }
});

// Inizialize the bars 
document.addEventListener('DOMContentLoaded', makeEmotionElements);