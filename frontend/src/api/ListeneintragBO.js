import BusinessObject from "./BusinessObject";

export default class ListeneintragBO extends BusinessObject {

/** Damit direkt über diese KLasse ein Name angelegt werden kann,
     muss der Parameter im Constructor entgegengenommen werden
     und an die Superklasse NamedBO weitergegeben werden. */

    constructor() {
        super();
        this.menge= null
        this.erledigt= false
        this.aenderungs_zeitpunkt= null
        this.einkaufsliste_id= null
        this.einzelhaendler_id= null
        this.einzelhaendler_name= null
        this.artikel_id= null
        this.artikel_name= null
        this.artikel_einheit= null
        this.benutzer_id= null
        this.benutzer_name=null
        this.zuletzt_geaendert= false
    }

    setZuletzt_geaendert(zuletzt_geaendert) {
        this.zuletzt_geaendert = zuletzt_geaendert
    }

    getZuletzt_geaendert() {
        return this.zuletzt_geaendert
    }

    setMenge(menge) {
        this.menge = menge
    }

    getMenge() {
        return this.menge
    }

    setErledigt(erledigt) {
        this.erledigt = erledigt
    }

    getErledigt() {
        return this.erledigt
    }

    setAenderungs_zeitpunkt(aenderungs_zeitpunkt) {
        this.aenderungs_zeitpunkt = aenderungs_zeitpunkt
    }

    getAenderungs_zeitpunkt() {
        return this.aenderungs_zeitpunkt
    }

    setEinkaufsliste_id(einkaufsliste_id) {
        this.einkaufsliste_id = einkaufsliste_id
    }

    getEinkaufsliste_id() {
        return this.einkaufsliste_id
    }

    setEinzelhaendler_id(einzelhaendler_id) {
        this.einzelhaendler_id = einzelhaendler_id
    }

    getEinzelhaendler_id() {
        return this.einzelhaendler_id
    }

      setEinzelhaendler_name(einzelhaendler_name) {
        this.einzelhaendler_name = einzelhaendler_name
    }

    getEinzelhaendler_name() {
        return this.einzelhaendler_name
    }

    setArtikel_id(artikel_id) {
        this.artikel_id = artikel_id
    }

    getArtikel_id() {
        return this.artikel_id
    }

    setArtikel_name(artikel_name) {
        this.artikel_name = artikel_name
    }

    getArtikel_name() {
        return this.artikel_name
    }

    setArtikel_einheit(artikel_einheit) {
        this.artikel_einheit = artikel_einheit
    }

    getArtikel_einheit() {
        return this.artikel_einheit
    }

    setBenutzer_id(benutzer_id) {
        this.benutzer_id = benutzer_id
    }

    getBenutzer_id() {
        return this.benutzer_id
    }

    setBenutzer_name(benutzer_name) {
        this.benutzer_name = benutzer_name
    }

    getBenutzer_name() {
        return this.benutzer_name
    }

    /** Gibt ein Array von ListeneintragBOs von einer gegebenen JSON Struktur zurück */
    static fromJSON(lis) {
        let result = [];
        if (Array.isArray(lis)) {
            lis.forEach((c) => {
                Object.setPrototypeOf(c, ListeneintragBO.prototype)
                result.push(c)
            })
        } else {
            // Es handelt sich um ein einzelnes Objekt
            let c = lis;
            Object.setPrototypeOf(c, ListeneintragBO.prototype)
            result.push(c)
        }
        return result;
    }
}