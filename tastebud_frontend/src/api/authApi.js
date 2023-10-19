async function basicFetch(url, payload) {
    const res = await fetch(url, payload)
    const body = await res.json()
    return body
  }
  
  
  export async function signup(context) {
    console.log(context)
    const payload = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(context)
    }
    const body = await basicFetch("http://localhost:8000/users/signup/",payload)
    return body
  }
  
  export async function login(context) {
    console.log(context)
    const payload = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(context)
    }
    const body = await basicFetch("http://localhost:8000/users/get-token/", payload)
    return body.token
  }

  export async function recipeSearch(queryParams) {

    const queryString = Object.keys(queryParams)
    .filter(key => queryParams[key] !== '')
    .map(key => `${key}=${queryParams[key]}`)
    .join('&')

    const url = `http://localhost:8000/api/v1/recipe_search/?${queryString}`

    const payload = {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
    }

    console.log(url)
    const body = await basicFetch(url, payload)
    return body
  }