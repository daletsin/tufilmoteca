function comprobarStorage(){
	if('localStorage' in window && window['localStorage'] !== null) {
   return true;
} else { return false; }
}