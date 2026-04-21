const isServer = typeof window === "undefined";

const getApiBase = () => {
  const isBrowser = typeof window !== "undefined";
  
  // 1. In browser, we ALWAYS prefer relative paths to leverage proxies and SSL correctly
  if (isBrowser) {
    return "";
  }

  // 2. Explicit Override for SSR/Scripts
  const envUrl = import.meta.env.VITE_API_URL as string;
  if (envUrl) return envUrl;

  // 3. Fallback for Local Development SSR
  const backendPort = import.meta.env.VITE_BACKEND_PORT;
  if (backendPort) {
    return `http://127.0.0.1:${backendPort}`;
  }

  return ""; 
};

export const API_BASE_URL = getApiBase();

// Utility to get the "clean" fetch and handle path normalization
const safeFetch = async (url: string, options?: RequestInit) => {
  let targetUrl = url;
  
  if (typeof window !== "undefined") {
    // If somehow an absolute localhost URL leaked in on a public domain, fix it
    const isPublicHost = !window.location.hostname.includes("127.0.0.1") && !window.location.hostname.includes("localhost");
    if (isPublicHost && (url.includes("127.0.0.1") || url.includes("localhost"))) {
       console.warn("[API Sanity Check] Sanitizing absolute localhost URL to relative path.");
       targetUrl = url.replace(/http:\/\/127\.0\.0\.1:\d+/, "").replace(/http:\/\/localhost:\d+/, "");
    }
  }
  
  return fetch(targetUrl, options);
};

export const getApiUrl = (path: string) => {
  const normalizedPath = path.startsWith("/") ? path : `/${path}`;
  
  // In the browser, we always return the relative path.
  // This ensures the request goes to the same origin/port, catching the Vite or Nginx proxy.
  if (typeof window !== "undefined") {
    return normalizedPath;
  }

  if (!API_BASE_URL) return normalizedPath;
  return `${API_BASE_URL.replace(/\/$/, "")}${normalizedPath}`;
};

// Diagnostic logging
if (typeof window !== "undefined") {
  console.log("%c[API Config] Mode: Browser (Relative Paths Enforced)", "color: #00ffaa; font-weight: bold; background: #002211; padding: 2px 6px; border-radius: 4px;");
}

export async function fetchProperties() {
  const res = await safeFetch(getApiUrl("/api/properties/"));
  if (!res.ok) throw new Error("Failed to fetch properties");
  return res.json();
}

export async function fetchPropertyBySlug(slug: string) {
  const res = await safeFetch(getApiUrl(`/api/properties/${slug}`));
  if (!res.ok) throw new Error("Property not found");
  return res.json();
}

export async function createProperty(data: any, token: string) {
  const res = await safeFetch(getApiUrl("/api/properties/"), {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Failed to create property");
  return res.json();
}

export async function updateProperty(id: string, data: any, token: string) {
  const res = await safeFetch(getApiUrl(`/api/properties/${id}`), {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    },
    body: JSON.stringify(data),
  });
  if (!res.ok) throw new Error("Failed to update property");
  return res.json();
}

export async function deleteProperty(id: string, token: string) {
  const res = await safeFetch(getApiUrl(`/api/properties/${id}`), {
    method: "DELETE",
    headers: {
      "Authorization": `Bearer ${token}`
    },
  });
  if (!res.ok) throw new Error("Failed to delete property");
  return res.json();
}

export async function uploadAsset(file: File) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await safeFetch(getApiUrl("/api/assets/upload"), {
    method: "POST",
    body: formData,
  });

  if (!res.ok) {
    const error = await res.json();
    throw new Error(error.detail || "Failed to upload asset");
  }

  return res.json();
}

export async function fetchInquiries(token: string) {
  const res = await safeFetch(getApiUrl("/api/inquiries/"), {
    headers: {
      "Authorization": `Bearer ${token}`
    }
  });
  if (!res.ok) throw new Error("Failed to fetch inquiries");
  return res.json();
}

export async function deleteInquiry(id: string, token: string) {
  const res = await safeFetch(getApiUrl(`/api/inquiries/${id}`), {
    method: "DELETE",
    headers: {
      "Authorization": `Bearer ${token}`
    }
  });
  if (!res.ok) throw new Error("Failed to delete inquiry");
  return res.json();
}

export async function submitInquiry(data: any) {
  const res = await safeFetch(getApiUrl("/api/inquiries/"), {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function fetchSettings() {
  try {
    const res = await safeFetch(getApiUrl("/api/settings"));
    if (!res.ok) {
      console.warn(`Settings fetch failed with status ${res.status}. Using fallback defaults.`);
      return null;
    }
    return res.json();
  } catch (error) {
    console.error("Critical error fetching site settings:", error);
    return null; // Return null instead of throwing to prevent SSR crash
  }
}

