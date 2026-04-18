const API_BASE_URL = "http://localhost:8000/api";

export interface Apartment {
  name: string;
  type: string;
  size: string;
  price: string;
  slug: string;
}

export interface Property {
  id?: string;
  slug: string;
  name: string;
  hero: string;
  intro: string;
  showApartmentNote: string;
  hours: string;
  apartments: Apartment[];
  tag?: string;
  date?: string;
  featured_image?: string;
  is_featured?: boolean;
}

async function getAuthHeaders() {
  const token = localStorage.getItem("admin_token");
  return {
    "Content-Type": "application/json",
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
  };
}

export async function fetchProperties(): Promise<Property[]> {
  const response = await fetch(`${API_BASE_URL}/properties/`, {
    headers: await getAuthHeaders(),
  });
  if (!response.ok) {
    throw new Error("Failed to fetch properties");
  }
  return response.json();
}

export async function fetchPropertyBySlug(slug: string): Promise<Property> {
  const response = await fetch(`${API_BASE_URL}/properties/${slug}`, {
    headers: await getAuthHeaders(),
  });
  if (!response.ok) {
    if (response.status === 404) {
      throw new Error("Property not found");
    }
    throw new Error("Failed to fetch property details");
  }
  return response.json();
}

export async function fetchAssets(): Promise<string[]> {
  const response = await fetch(`${API_BASE_URL}/assets/`, {
    headers: await getAuthHeaders(),
  });
  if (!response.ok) {
    throw new Error("Failed to fetch assets");
  }
  return response.json();
}

export async function uploadAsset(file: File): Promise<{ filename: string; path: string }> {
  const token = localStorage.getItem("admin_token");
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${API_BASE_URL}/assets/upload`, {
    method: "POST",
    headers: {
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
    },
    body: formData,
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || "Failed to upload image");
  }

  return response.json();
}
