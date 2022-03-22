let raceNumber = Math.floor(Math.random() * 1000);
let earlyReg = false;
let runnersAge = 18;

if (earlyReg === true && runnersAge > 18) {
  raceNumber += 1000; 
}

if (earlyReg === true && runnersAge > 18) {
  console.log("Your race time start at 9:30 AM.");
}else if (earlyReg === true || runnersAge > 18) {
  console.log(`Your race time is 11:00 AM and your number is ${raceNumber}.`)
}else if (runnersAge < 18) {
  console.log(`Your race time is 12:30 PM and your number is ${raceNumber}.`)
}else {
  console.log('See regestration desk.')
}