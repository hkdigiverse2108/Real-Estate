import { createFileRoute, Link, notFound } from "@tanstack/react-router";
import { Header } from "@/components/sandars/Header";
import { Footer } from "@/components/sandars/Footer";
import { fetchPropertyBySlug } from "@/lib/api";
import { useState } from "react";
import { MapPin, Layout, Ruler, ChevronRight } from "lucide-react";

export const Route = createFileRoute("/properties/$slug/apartments/$aptSlug")({
  loader: async ({ params }) => {
    try {
      const property = await fetchPropertyBySlug(params.slug);
      const apartment = property.apartments.find((a: any) => a.slug === params.aptSlug);
      if (!apartment) throw notFound();
      return { property, apartment };
    } catch (error) {
      throw notFound();
    }
  },
  component: ApartmentDetailPage,
});

function ApartmentDetailPage() {
  const { property, apartment } = Route.useLoaderData();
  const [submitted, setSubmitted] = useState(false);

  const handleInquiry = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    const data = {
      ...Object.fromEntries(formData.entries()),
      property: property.name,
      apartment: apartment.name,
      createdAt: new Date().toISOString(),
    };

    try {
      const response = await fetch("http://localhost:8000/api/inquiries", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });

      if (response.ok) {
        setSubmitted(true);
        setTimeout(() => setSubmitted(false), 5000);
        (e.target as HTMLFormElement).reset();
      }
    } catch (err) {
      alert("Failed to send inquiry. Please try again.");
    }
  };

  return (
    <main className="bg-paper text-ink">
      <Header />

      {/* Hero Section */}
      <section className="relative pt-24 md:pt-28">
        <div className="container-luxe">
          <div className="relative h-[60vh] min-h-[400px] w-full overflow-hidden">
            <img
              src={apartment.hero_image || property.hero}
              alt={apartment.name}
              className="absolute inset-0 h-full w-full object-cover"
            />
            <div className="absolute inset-0 bg-ink/30" />
            <div className="relative h-full flex flex-col items-center justify-center text-center px-6">
              <nav className="flex items-center gap-2 mb-6 text-[10px] tracking-display uppercase text-paper/60">
                <Link to="/" className="hover:text-paper transition-colors">Home</Link>
                <ChevronRight className="h-3 w-3" />
                <Link to={`/properties/${property.slug}`} className="hover:text-paper transition-colors">{property.name}</Link>
                <ChevronRight className="h-3 w-3" />
                <span className="text-paper">Details</span>
              </nav>
              <h1 className="font-display text-white text-4xl md:text-6xl lg:text-7xl uppercase tracking-tight">
                {apartment.name}
              </h1>
              <div className="mt-6 flex items-center gap-8 text-[11px] tracking-display uppercase text-paper/90">
                <span>{apartment.type}</span>
                <span className="h-4 w-[1px] bg-paper/20" />
                <span>{apartment.size}</span>
                <span className="h-4 w-[1px] bg-paper/20" />
                <span>{apartment.price}</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Main Content - Floorplan & Dimensions */}
      <section className="py-20 md:py-32">
        <div className="container-luxe">
          <div className="grid lg:grid-cols-2 gap-16 lg:gap-24 items-start">
            
            {/* Left: Floorplan Visuals */}
            <div className="space-y-12">
              <div className="bg-white p-8 md:p-12 shadow-sm border border-border/50">
                <h2 className="font-display text-3xl uppercase tracking-tight mb-10 text-ink/80 flex items-center gap-3">
                  <Layout className="h-6 w-6 text-rose" />
                  Floorplan
                </h2>
                {apartment.floorplan_image ? (
                  <img 
                    src={apartment.floorplan_image} 
                    alt="Floorplan" 
                    className="w-full h-auto"
                  />
                ) : (
                  <div className="aspect-[4/5] bg-paper-soft flex items-center justify-center text-ink/20 italic text-sm">
                    Floorplan coming soon
                  </div>
                )}
              </div>

              {apartment.location_map_image && (
                <div className="bg-white p-8 md:p-12 shadow-sm border border-border/50 max-w-md">
                  <h3 className="font-display text-xl uppercase tracking-tight mb-6 text-ink/80 flex items-center gap-2">
                    <MapPin className="h-5 w-5 text-rose" />
                    Relative Location
                  </h3>
                  <img 
                    src={apartment.location_map_image} 
                    alt="Location map" 
                    className="w-full h-auto"
                  />
                </div>
              )}
            </div>

            {/* Right: Dimensions Table */}
            <div className="lg:sticky lg:top-32">
              <h2 className="font-display text-3xl uppercase tracking-tight mb-10 text-ink/80 flex items-center gap-3">
                <Ruler className="h-6 w-6 text-rose" />
                Dimensions
              </h2>
              
              <div className="overflow-x-auto">
                <table className="w-full text-left">
                  <thead>
                    <tr className="border-b border-border text-[11px] tracking-display uppercase text-ink/40">
                      <th className="py-4 font-bold">Room</th>
                      <th className="py-4 font-bold">Metric</th>
                      <th className="py-4 font-bold">Imperial</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-border/50">
                    {apartment.dimensions && apartment.dimensions.length > 0 ? (
                      apartment.dimensions.map((dim: any, i: number) => (
                        <tr key={i} className="text-sm md:text-base text-ink/80">
                          <td className="py-5 pr-4 font-medium">{dim.room}</td>
                          <td className="py-5 pr-4 text-ink/60">{dim.metric}</td>
                          <td className="py-5 text-ink/60">{dim.imperial}</td>
                        </tr>
                      ))
                    ) : (
                      <tr>
                        <td colSpan={3} className="py-10 text-center text-ink/30 italic text-sm">
                          Specifications available on request
                        </td>
                      </tr>
                    )}
                  </tbody>
                </table>
              </div>

              <div className="mt-12 p-8 bg-paper-soft border border-border/50">
                <p className="text-xs italic text-ink/40 leading-relaxed uppercase tracking-wide">
                  Not to scale. All area measures and dimensions are approximate and for illustrative purposes only. 
                  Actual room layout and specifications may vary.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Inquiry Form Section */}
      <section className="py-20 md:py-32 bg-[#DED1C1]/20">
        <div className="container-luxe max-w-4xl">
          <div className="text-center mb-16">
            <h2 className="font-display text-4xl md:text-5xl uppercase tracking-tight text-ink/85">
              Book a visit or request a call back
            </h2>
            <p className="mt-6 text-ink/60 max-w-xl mx-auto">
              Fill in your details below and a member of our team will contact you shortly to discuss {apartment.name}.
            </p>
          </div>

          <form onSubmit={handleInquiry} className="grid md:grid-cols-2 gap-8">
            <div className="md:col-span-2">
              <Field label="Title" name="title" placeholder="Title" />
            </div>
            <Field label="First Name" name="firstName" placeholder="First Name" required />
            <Field label="Surname" name="surname" placeholder="Surname" required />
            <Field label="Email" name="email" type="email" placeholder="Email" required />
            <Field label="Telephone" name="telephone" type="tel" placeholder="Telephone" />
            <div className="md:col-span-2">
              <Field label="Postcode" name="postcode" placeholder="Post Code" />
            </div>
            
            <div className="md:col-span-2 pt-4">
              <button
                type="submit"
                className="w-full md:w-auto px-12 py-4 bg-[#576D69] text-white text-[11px] tracking-display uppercase transition-all hover:bg-rose active:scale-95 disabled:opacity-50"
                disabled={submitted}
              >
                {submitted ? "Inquiry Received" : "Submit Inquiry"}
              </button>
              {submitted && (
                <p className="mt-4 text-rose font-medium text-center">
                  Thank you. We have received your request for {apartment.name}.
                </p>
              )}
            </div>
          </form>
        </div>
      </section>

      <Footer />
    </main>
  );
}

function Field({ label, name, type = "text", placeholder, required }: any) {
  return (
    <div className="space-y-2">
      <label htmlFor={name} className="block text-[11px] font-bold tracking-display uppercase text-ink/60">
        {label} {required && <span className="text-rose">*</span>}
      </label>
      <input
        id={name}
        name={name}
        type={type}
        placeholder={placeholder}
        required={required}
        className="w-full bg-white border border-border px-4 py-3 text-ink placeholder:text-ink/30 focus:outline-none focus:border-rose transition-colors"
      />
    </div>
  );
}
