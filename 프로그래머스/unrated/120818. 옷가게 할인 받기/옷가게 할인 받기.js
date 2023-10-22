function solution(price) {
    
    if ( 300000 > price && price >= 100000) {
        return  Math.floor(0.95 * price)
    }
    else if (500000 > price && price >= 300000){
        return  Math.floor(0.9 * price)
    }
    else if (price >= 500000){
        return  Math.floor(0.8 * price)
    }
    else {
        return  Math.floor(price)
    }
   
}