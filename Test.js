var result ="[{'Source': 'Internet Movie Database', 'Value': '6.6/10'}, {'Source': 'Rotten Tomatoes', 'Value': '85%'}, {'Source': 'Metacritic', 'Value': '63/100'}]"
result = result.replaceAll("\'", "\"")
jsonFormat = JSON.parse(result);
console.log(jsonFormat)
// console.log(result)