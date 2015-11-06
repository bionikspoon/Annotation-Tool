(function() {
  'use strict';

  angular
    .module('app.auth')
    .constant('PERMISSION', {
      pubmed: {
        pubmed: {
          add:    'pubmed.add_pubmed',
          change: 'pubmed.change_pubmed'

        }
      }
    });
})();
/*var permissions = [
 "gene.change_gene",
 "pubmed.delete_syntaxlookup",
 "gene.change_uniprotidslookup",
 "gene.add_lsdblookup",
 "gene.delete_omimidlookup",
 "contenttypes.add_contenttype",
 "pubmed.change_varianttypelookup",
 "pubmed.change_syntaxlookup",
 "gene.change_enalookup",
 "gene.delete_ccdsidlookup",
 "gene.delete_pubmedidlookup",
 "pubmed.add_patientoutcomeslookup",
 "pubmed.custom_add_mutationtypelookup",
 "pubmed.add_structurelookup",
 "socialaccount.add_socialaccount",
 "sessions.delete_session",
 "gene.delete_prevsymbollookup",
 "pubmed.delete_patientoutcomeslookup",
 "pubmed.add_rulelevellookup",
 "gene.delete_prevnamelookup",
 "pubmed.delete_diseaselookup",
 "users.delete_user",
 "gene.delete_gene",
 "contenttypes.change_contenttype",
 "authtoken.delete_token",
 "gene.change_genefamilyidlookup",
 "socialaccount.delete_socialaccount",
 "pubmed.add_mutationtypelookup",
 "authtoken.change_token",
 "auth.add_group",
 "gene.add_aliassymbollookup",
 "pubmed.delete_structurelookup",
 "gene.add_uniprotidslookup",
 "gene.delete_lsdblookup",
 "gene.change_omimidlookup",
 "gene.change_prevsymbollookup",
 "authtoken.add_token",
 "gene.change_pubmedidlookup",
 "account.change_emailaddress",
 "auth.change_permission",
 "pubmed.delete_varianttypelookup",
 "gene.add_omimidlookup",
 "pubmed.change_mutationtypelookup",
 "auth.delete_permission",
 "gene.change_genefamilylookup",
 "gene.delete_genefamilyidlookup",
 "contenttypes.delete_contenttype",
 "sessions.add_session",
 "account.change_emailconfirmation",
 "gene.delete_enalookup",
 "gene.delete_genefamilylookup",
 "gene.change_mgdidlookup",
 "pubmed.add_syntaxlookup",
 "pubmed.change_pubmed",
 "pubmed.delete_rulelevellookup",
 "socialaccount.change_socialapp",
 "gene.delete_refseqaccessionlookup",
 "gene.add_pubmedidlookup",
 "pubmed.delete_pubmed",
 "socialaccount.delete_socialtoken",
 "sites.delete_site",
 "account.delete_emailaddress",
 "pubmed.add_varianttypelookup",
 "admin.add_logentry",
 "auth.change_group",
 "gene.add_enzymeidlookup",
 "gene.change_enzymeidlookup",
 "pubmed.delete_mutationtypelookup",
 "users.change_user",
 "gene.add_rgdidlookup",
 "gene.delete_aliassymbollookup",
 "sessions.change_session",
 "gene.change_rgdidlookup",
 "gene.add_genefamilylookup",
 "pubmed.custom_add_structurelookup",
 "pubmed.change_variantconsequencelookup",
 "sites.add_site",
 "pubmed.change_structurelookup",
 "socialaccount.add_socialapp",
 "gene.add_enalookup",
 "account.add_emailaddress",
 "gene.delete_rgdidlookup",
 "gene.add_prevsymbollookup",
 "users.add_user",
 "pubmed.delete_variantconsequencelookup",
 "gene.change_ccdsidlookup",
 "gene.add_aliasnamelookup",
 "gene.delete_uniprotidslookup",
 "gene.add_genefamilyidlookup",
 "pubmed.change_diseaselookup",
 "account.add_emailconfirmation",
 "account.delete_emailconfirmation",
 "gene.change_prevnamelookup",
 "socialaccount.change_socialtoken",
 "gene.change_lsdblookup",
 "gene.add_mgdidlookup",
 "sites.change_site",
 "pubmed.add_variantconsequencelookup",
 "gene.delete_mgdidlookup",
 "socialaccount.add_socialtoken",
 "gene.change_aliassymbollookup",
 "gene.add_refseqaccessionlookup",
 "pubmed.add_diseaselookup",
 "auth.delete_group",
 "gene.add_ccdsidlookup",
 "gene.delete_enzymeidlookup",
 "admin.change_logentry",
 "gene.delete_aliasnamelookup",
 "gene.add_gene",
 "pubmed.custom_change_structurelookup",
 "pubmed.add_pubmed",
 "gene.change_refseqaccessionlookup",
 "gene.add_prevnamelookup",
 "auth.add_permission",
 "pubmed.custom_change_mutationtypelookup",
 "pubmed.change_patientoutcomeslookup",
 "socialaccount.change_socialaccount",
 "socialaccount.delete_socialapp",
 "admin.delete_logentry",
 "pubmed.change_rulelevellookup",
 "gene.change_aliasnamelookup"
 ];*/
