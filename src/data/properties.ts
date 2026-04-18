import heroCullinan from "@/assets/hero-cullinan-pool.jpg";
import heroPollards from "@/assets/hero-pollards.jpg";
import heroEastley from "@/assets/hero-eastley.jpg";
import heroMeadlake from "@/assets/hero-meadlake.jpg";

export type Apartment = {
  name: string;
  type: string;
  size: string;
  price: string;
  slug: string;
};

export type Property = {
  slug: string;
  name: string;
  hero: string;
  intro: string;
  showApartmentNote: string;
  hours: string;
  apartments: Apartment[];
};

export const PROPERTIES: Record<string, Property> = {
  "cullinan-house": {
    slug: "cullinan-house",
    name: "Cullinan House",
    hero: heroCullinan,
    intro:
      "The central hub of The Sandars later living village, Cullinan House is a Grade II listed building that places you at the centre of the community. Here you'll find the perfect haven for your retirement with open-plan apartments available to buy or rent.",
    showApartmentNote: "Show apartment available to view",
    hours: "Open from 10am \u2013 5pm Monday \u2013 Friday",
    apartments: [
      { name: "No.1 Cullinan House", type: "1 Bedroom", size: "76 sq m", price: "On request", slug: "no-1-cullinan-house" },
      { name: "No.2 Cullinan House", type: "1 Bedroom", size: "72 sq m", price: "On request", slug: "no-2-cullinan-house" },
      { name: "No.4 Cullinan House", type: "2 Bedroom", size: "91 sq m", price: "On request", slug: "no-4-cullinan-house" },
      { name: "No.7 Cullinan House", type: "2 Bedroom", size: "101 sq m", price: "On request", slug: "no-7-cullinan-house" },
      { name: "No.15 Cullinan House", type: "2 Bedroom", size: "83 sq m", price: "On request", slug: "no-15-cullinan-house" },
      { name: "No.22 Cullinan House", type: "2 Bedroom", size: "102 sq m", price: "On request", slug: "no-22-cullinan-house" },
    ],
  },
  "pollards-court": {
    slug: "pollards-court",
    name: "Pollards Court",
    hero: heroPollards,
    intro:
      "Beautifully appointed apartments set within the heart of the estate, Pollards Court combines warm contemporary interiors with quiet, garden-facing aspects.",
    showApartmentNote: "Show apartment available to view",
    hours: "Open from 10am \u2013 5pm Monday \u2013 Friday",
    apartments: [
      { name: "No.1 Pollards Court", type: "2 Bedroom", size: "124 sq m", price: "On request", slug: "no-1-pollards-court" },
      { name: "No.4 Pollards Court", type: "2 Bedroom", size: "124 sq m", price: "On request", slug: "no-4-pollards-court" },
    ],
  },
  "eastley-end-house": {
    slug: "eastley-end-house",
    name: "Eastley End House",
    hero: heroEastley,
    intro:
      "Exuding Georgian charm and character, Eastley End House is a three-storey building originally built in the late 18th century and contains a number of luxury apartments.",
    showApartmentNote: "Show apartment available to view",
    hours: "Open from 10am \u2013 5pm Monday \u2013 Friday",
    apartments: [
      { name: "No.4 Eastley End House", type: "2 Bedroom", size: "118 sq m", price: "On request", slug: "no-4-eastley-end-house" },
      { name: "No.6 Eastley End House", type: "1 Bedroom", size: "92 sq m", price: "On request", slug: "no-6-eastley-end-house" },
    ],
  },
  "meadlake-house": {
    slug: "meadlake-house",
    name: "Meadlake House",
    hero: heroMeadlake,
    intro:
      "A Grade II listed Georgian house offering one and two bedroom luxury living apartments, including duplex and penthouse options.",
    showApartmentNote: "Show apartment available to view",
    hours: "Open from 10am \u2013 5pm Monday \u2013 Friday",
    apartments: [
      { name: "No.2 Meadlake House", type: "1 Bedroom", size: "88 sq m", price: "On request", slug: "no-2-meadlake-house" },
      { name: "No.5 Meadlake House", type: "2 Bedroom Duplex", size: "156 sq m", price: "On request", slug: "no-5-meadlake-house" },
      { name: "Penthouse, Meadlake House", type: "2 Bedroom Penthouse", size: "182 sq m", price: "On request", slug: "penthouse-meadlake-house" },
    ],
  },
};
