console.log("1"); 
function imprimir(callback){ 
 setTimeout(() => { 
 console.log("2"); 
 callback(); 
 }, 2000); 
} 
function imprimir3() { 
 console.log("3"); 
} 
imprimir(imprimir3); 
