import wellbeing from "@/assets/life-wellbeing.jpg";
import parkland from "@/assets/life-parkland.jpg";
import hub from "@/assets/life-hub.jpg";
import architecture from "@/assets/life-architecture.jpg";
import enjoyment from "@/assets/life-enjoyment.jpg";
import belonging from "@/assets/life-belonging.jpg";

const ITEMS = [
  { image: wellbeing, title: "Health & wellbeing", body: "Health and wellbeing is at the heart of everything we do. Our extensive fitness suite is second to none, providing bespoke solutions for all." },
  { image: parkland, title: "27 acres of lakes & parkland", body: "Our serene lake and picturesque gardens are an idyllic spot to unwind \u2014 a peaceful walk, watching the sunset, or simply relaxing by the water." },
  { image: hub, title: "The Community Hub", body: "The vibrant heart of The Sandars \u2014 a seamless blend of relaxation, wellness and social engagement, designed for a life of comfort and sophistication." },
  { image: architecture, title: "Eclectic architecture", body: "A spectrum of choice across the 18th, 19th, 20th and 21st centuries \u2014 creating the broadest possible appeal to suit any taste." },
  { image: enjoyment, title: "A life of enjoyment", body: "Regular social events and activities offer plenty of opportunity to connect \u2014 from yoga and art classes to private dinners and recitals." },
  { image: belonging, title: "True belonging", body: "A bespoke yet \u2018village feel\u2019 enhances the sense of belonging \u2014 a community where you are known, welcomed and at home." },
];

export const LifeGrid = () => (
  <section className="py-20 md:py-28 bg-paper-soft">
    <div className="container-luxe">
      <div className="text-center max-w-2xl mx-auto mb-14 md:mb-20">
        <p className="text-xs tracking-display uppercase text-rose mb-5">Image caption</p>
        <h2 className="font-display text-4xl md:text-5xl leading-[1.1] text-ink">
          Life at the Sandars
        </h2>
      </div>

      <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-x-8 gap-y-14">
        {ITEMS.map((it) => (
          <article key={it.title} className="group">
            <div className="aspect-[4/3] overflow-hidden mb-6 bg-ink/5">
              <img
                src={it.image}
                alt={it.title}
                className="h-full w-full object-cover transition-transform duration-[1200ms] ease-out group-hover:scale-105"
                loading="lazy"
                width={1024}
                height={768}
              />
            </div>
            <h3 className="font-display text-2xl md:text-[26px] text-ink mb-3">{it.title}</h3>
            <p className="text-ink/70 text-[15px] leading-relaxed">{it.body}</p>
          </article>
        ))}
      </div>
    </div>
  </section>
);
