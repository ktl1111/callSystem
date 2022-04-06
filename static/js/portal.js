//input must be integer

const numberForm = document.querySelector('#numberForm3');
const numberForm2 = document.querySelector('#numberForm2');
numberForm.addEventListener('submit', e => {
    // prevent default action
    // e.preventDefault();
});
numberForm2.addEventListener('submit', e => {
    // prevent default action
    // e.preventDefault();
});

//show num to 500
const allnums = async() =>{
    let n =1;
    for (let i = 1; i < 501; i++) {
        n++;
        document.getElementById('show').innerHTML += `<span class="num" id="${i}">${i}</span>`;
        num_shownum = document.getElementById('shownum')
        if(n == 11){
            document.getElementById('show').innerHTML += "<br/>"
            n=1;
        };
    };
    return {num_shownum:num_shownum};
};

allnums();

//保留上一次送出的號碼
// set the value to this input
document.getElementById("number").value = getSavedValue("number");
document.getElementById("onspot_number").value = getSavedValue("onspot_number");
 //Save the value function - save it to localStorage as (ID, VALUE)
function saveValue(e){
    var id = e.id;  // get the sender's id to save it .
    var val = e.value; // get the value.
    localStorage.setItem(id, val);// Every time user writing something, the localStorage's value will override .
}

//get the saved value function - return the value of "v" from localStorage.
function getSavedValue (v){
    if (!localStorage.getItem(v)) {
        return "";// You can change this to your defualt value.
    }
    return localStorage.getItem(v);
}

// localStorage.clear();
