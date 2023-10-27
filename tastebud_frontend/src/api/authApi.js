async function basicFetch(url, payload) {
    const res = await fetch(url, payload)
    const body = await res.json()
    return body
  }
  
  
  export async function signup(context) {
    const base_url = `http://${import.meta.env.VITE_BASE_URL}`
    const endpoint = '/users/signup/'
    console.log(base_url)
    const url = new URL(endpoint, base_url)
    console.log(context)
    const payload = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(context)
    }
    const body = await basicFetch(url, payload)
    return body
  }
  
  export async function login(context) {
    const base_url = `http://${import.meta.env.VITE_BASE_URL}`
    const endpoint = '/users/get-token/'
    const url = new URL(endpoint, base_url)

    console.log(context)
    const payload = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(context)
    }
    const body = await basicFetch(url, payload)
    return body.token
  }

  export async function recipeSearch(queryParams, authToken) {
    const base_url = `http://${import.meta.env.VITE_BASE_URL}`
    const queryString = Object.keys(queryParams)
      .map((key) => {
        if (key === 'health' && Array.isArray(queryParams[key])) {
          return queryParams[key].map((value) => `${key}=${value}`).join('&');
        } else {
          return `${key}=${queryParams[key]}`;
        }
      })
      .join('&');
  
    const url = `${base_url}/api/v1/recipe_search/?${queryString}`;
  
    const payload = {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `token ${authToken}`,
      },
    }
  
    const body = await basicFetch(url, payload);
    return body;
  }