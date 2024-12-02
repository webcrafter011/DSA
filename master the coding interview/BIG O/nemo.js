const names = ["notnemo"];

function findnemo(array) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === "nemo") {
      console.log("Found NEMO!");
      break;
    } else {
      console.log("Didnt find NEMO!");
    }
  }
}

findnemo(names);
