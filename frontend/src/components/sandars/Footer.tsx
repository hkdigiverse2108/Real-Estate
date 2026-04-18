import { Logo } from "./Logo";

export const Footer = () => (
  <footer className="bg-paper border-t border-border pt-16 md:pt-20 pb-10">
    <div className="container-luxe">
      <div className="grid md:grid-cols-2 gap-12 mb-12">
        <div>
          <Logo className="!text-3xl" />
          <p className="mt-10 text-sm text-ink/60 max-w-sm">
            A unique, state of the art development for luxury later living, exclusively for
            those 55 years and over.
          </p>
          <div className="mt-10 inline-flex items-center gap-2 px-3 py-2 bg-gold/90 text-ink font-semibold tracking-wider text-sm">
            EDEN
            <span className="font-normal text-xs italic">retirement living</span>
          </div>
        </div>

        <div className="md:text-right">
          <address className="not-italic text-ink leading-relaxed font-medium">
            The Sandars,
            <br />
            Coldharbour Lane,
            <br />
            Egham,
            <br />
            Surrey,
            <br />
            TW20 8TD
          </address>

          <div className="mt-10 inline-block bg-[oklch(0.85_0.18_95)] text-[oklch(0.55_0.22_27)] font-bold tracking-wide px-3 py-1.5">
            savills
          </div>

          <div className="mt-8 space-y-2">
            <a href="tel:02037572828" className="block text-ink hover:text-rose font-medium transition-colors">
              0203 757 2828
            </a>
            <a
              href="mailto:SunningdaleNewHomes@savills.com"
              className="block text-ink hover:text-rose font-medium transition-colors"
            >
              SunningdaleNewHomes@savills.com
            </a>
          </div>
        </div>
      </div>

      <div className="border-t border-border pt-6 flex flex-col md:flex-row gap-3 md:items-center md:justify-between text-sm text-ink/60">
        <p>© Eden Retirement Living {new Date().getFullYear()}. All rights reserved.</p>
        <p>Designed and developed in tribute to The Sandars.</p>
      </div>
    </div>
  </footer>
);
