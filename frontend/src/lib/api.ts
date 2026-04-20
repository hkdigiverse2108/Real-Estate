const isServer = typeof window === "undefined";

const getAutoDetectedApiBase = () => {
  if (isServer) {
    // In SSR, we MUST have an absolute URL for cross-server fetches.
    // Nitro/TanStack Start environments usually provide VITE_API_URL.
    return (import.meta.env.VITE_API_URL as string) || "http://localhost:8000";
  }
  
  // Browser: Default to relative paths for maximum compatibility with proxies
  return ""; 
};

export const API_BASE_URL = (import.meta.env.VITE_API_URL as string) || getAutoDetectedApiBase();

export const getApiUrl = (path: string) => {
  const normalizedPath = path.startsWith("/") ? path : `/${path}`;
  if (!API_BASE_URL) return normalizedPath;
  return `${API_BASE_URL.replace(/\/$/, "")}${normalizedPath}`;
};

export async function fetchProperties() {
  const res = await fetch(getApiUrl("/api/properties/"));
  if (!res.ok) throw new Error("Failed to fetch properties");
  return res.json();
}

export async function fetchPropertyBySlug(slug: string) {
  const res = await fetch(getApiUrl(`/api/properties/${slug}`));
  if (!res.ok) throw new Error("Property not found");
  return res.json();
}

export async function createProperty(data: any, token: string) {
  const res = await fetch(getApiUrl("/api/properties/"), {
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
  const res = await fetch(getApiUrl(`/api/properties/${id}`), {
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
  const res = await fetch(getApiUrl(`/api/properties/${id}`), {
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

  const res = await fetch(getApiUrl("/api/assets/upload"), {
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
  const res = await fetch(getApiUrl("/api/inquiries/"), {
    headers: {
      "Authorization": `Bearer ${token}`
    }
  });
  if (!res.ok) throw new Error("Failed to fetch inquiries");
  return res.json();
}

export async function deleteInquiry(id: string, token: string) {
  const res = await fetch(getApiUrl(`/api/inquiries/${id}`), {
    method: "DELETE",
    headers: {
      "Authorization": `Bearer ${token}`
    }
  });
  if (!res.ok) throw new Error("Failed to delete inquiry");
  return res.json();
}

export async function submitInquiry(data: any) {
  const res = await fetch(getApiUrl("/api/inquiries/"), {
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
    const res = await fetch(getApiUrl("/api/settings"));
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

