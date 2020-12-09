const get = (msec, payload) => {
  return new Promise(function(resolve, reject){
    setTimeout(resolve, msec);
  }).then(() => {
      return payload
  })
}

export const saveTodo = (payload) => {
	return get(1000, payload)
}
