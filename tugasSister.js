a = [1,2,3,4,5,6,7,8,9,10]
function perkalian(hasil){
    return hasil * 2;
}
function perkalian1(hasil){
    return hasil * 1;
}
const perkalian1Array = a.map( (item) => {setTimeout (() => { console.log(perkalian1(item))}, 1000)});
const perkalian2Array = a.map(perkalian);
console.log(perkalian2Array);