// document.getElementById("submit_btn").addEventListener("click", function(){
//     const truePositive = document.getElementById("true-positive").value;
//     const falseNegative = document.getElementById("false-negative").value;
//     const falsePositive = document.getElementById("false-positive").value;
//     const trueNegative = document.getElementById("true-negative").value;

//     const regex = /^[0-9]+$/;
    

//     if (regex.test(truePositive) && regex.test(falseNegative) && regex.test(falsePositive) && regex.test(trueNegative)) {
//       // Valid input, store the values
//       sessionStorage.setItem("true-positive", truePositive);
//       sessionStorage.setItem("false-negative", falseNegative);
//       sessionStorage.setItem("false-positive", falsePositive);
//       sessionStorage.setItem("true-negative", trueNegative);
//       alert("Data submitted successfully!");
//     } else {
//       alert("Invalid input. Please enter positive numbers only.");
//     }
// });



// document.getElementById("display_btn").addEventListener("click", function(){
//     const resultDiv = document.getElementById("result");
//     resultDiv.innerHTML = `
//       True Positive: ${sessionStorage.getItem("true-positive") || 'N/A'}<br>
//       False Negative: ${sessionStorage.getItem("false-negative") || 'N/A'}<br>
//       False Positive: ${sessionStorage.getItem("false-positive") || 'N/A'}<br>
//       True Negative: ${sessionStorage.getItem("true-negative") || 'N/A'}<br>
//     `;
// });

function validateData() {
    const truePositive = document.getElementById("truePositive").value;
    const falseNegative = document.getElementById("falseNegative").value;
    const falsePositive = document.getElementById("falsePositive").value;
    const trueNegative = document.getElementById("trueNegative").value;
  
    const regex = /^[0-9]+$/;
  
    if (regex.test(truePositive) && regex.test(falseNegative) && regex.test(falsePositive) && regex.test(trueNegative)) {
      // Valid input, store the values
      sessionStorage.setItem("truePositive", truePositive);
      sessionStorage.setItem("falseNegative", falseNegative);
      sessionStorage.setItem("falsePositive", falsePositive);
      sessionStorage.setItem("trueNegative", trueNegative);
      alert("Data submitted successfully!");
    } else {
      alert("Invalid input. Please enter positive numbers only.");
    }
  }
  
  function displayData() {
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = `
      True Positive: ${sessionStorage.getItem("truePositive") || 'N/A'}<br>
      False Negative: ${sessionStorage.getItem("falseNegative") || 'N/A'}<br>
      False Positive: ${sessionStorage.getItem("falsePositive") || 'N/A'}<br>
      True Negative: ${sessionStorage.getItem("trueNegative") || 'N/A'}<br>
    `;
  }
  