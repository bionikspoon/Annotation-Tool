(function() {
  'use strict';

  angular
    .module('app.auth')
    .constant('PERMISSION', {
      gene:          {
        gene:                  {
          change: "gene.change_gene",
          delete: "gene.delete_gene",
          add:    "gene.add_gene"
        },
        uniprotidslookup: {
          change: "gene.change_uniprotidslookup",
          add:    "gene.add_uniprotidslookup",
          delete: "gene.delete_uniprotidslookup"
        },
        lsdblookup:       {
          add:    "gene.add_lsdblookup",
          delete: "gene.delete_lsdblookup",
          change: "gene.change_lsdblookup"
        },
        omimidlookup:     {
          delete: "gene.delete_omimidlookup",
          change: "gene.change_omimidlookup",
          add:    "gene.add_omimidlookup"
        },
        enalookup:        {
          change: "gene.change_enalookup",
          delete: "gene.delete_enalookup",
          add:    "gene.add_enalookup"
        },
        ccdsidlookup:     {
          delete: "gene.delete_ccdsidlookup",
          change: "gene.change_ccdsidlookup",
          add:    "gene.add_ccdsidlookup"
        },
        pubmedidlookup:   {
          delete: "gene.delete_pubmedidlookup",
          change: "gene.change_pubmedidlookup",
          add:    "gene.add_pubmedidlookup"
        },
        prevsymbollookup: {
          delete: "gene.delete_prevsymbollookup",
          change: "gene.change_prevsymbollookup",
          add:    "gene.add_prevsymbollookup"
        },
        prevnamelookup:   {
          delete: "gene.delete_prevnamelookup",
          change: "gene.change_prevnamelookup",
          add:    "gene.add_prevnamelookup"
        },
        genefamilyidlookup: {
          change: "gene.change_genefamilyidlookup",
          delete: "gene.delete_genefamilyidlookup",
          add:    "gene.add_genefamilyidlookup"
        },
        aliassymbollookup:  {
          add:    "gene.add_aliassymbollookup",
          delete: "gene.delete_aliassymbollookup",
          change: "gene.change_aliassymbollookup"
        },
        genefamilylookup:   {
          change: "gene.change_genefamilylookup",
          delete: "gene.delete_genefamilylookup",
          add:    "gene.add_genefamilylookup"
        },
        mgdidlookup:        {
          change: "gene.change_mgdidlookup",
          add:    "gene.add_mgdidlookup",
          delete: "gene.delete_mgdidlookup"
        },
        refseqaccessionlookup: {
          delete: "gene.delete_refseqaccessionlookup",
          add:    "gene.add_refseqaccessionlookup",
          change: "gene.change_refseqaccessionlookup"
        },
        enzymeidlookup:        {
          add:    "gene.add_enzymeidlookup",
          change: "gene.change_enzymeidlookup",
          delete: "gene.delete_enzymeidlookup"
        },
        rgdidlookup:           {
          add:    "gene.add_rgdidlookup",
          change: "gene.change_rgdidlookup",
          delete: "gene.delete_rgdidlookup"
        },
        aliasnamelookup:       {
          add:    "gene.add_aliasnamelookup",
          delete: "gene.delete_aliasnamelookup",
          change: "gene.change_aliasnamelookup"
        }
      },
      pubmed: {
        syntaxlookup:             {
          delete: "pubmed.delete_syntaxlookup",
          change: "pubmed.change_syntaxlookup",
          add:    "pubmed.add_syntaxlookup"
        },
        varianttypelookup: {
          change: "pubmed.change_varianttypelookup",
          delete: "pubmed.delete_varianttypelookup",
          add:    "pubmed.add_varianttypelookup"
        },
        patientoutcomeslookup: {
          add:    "pubmed.add_patientoutcomeslookup",
          delete: "pubmed.delete_patientoutcomeslookup",
          change: "pubmed.change_patientoutcomeslookup"
        },
        structurelookup:       {
          add:    "pubmed.add_structurelookup",
          delete: "pubmed.delete_structurelookup",
          change: "pubmed.change_structurelookup"
        },
        rulelevellookup:       {
          add:    "pubmed.add_rulelevellookup",
          delete: "pubmed.delete_rulelevellookup",
          change: "pubmed.change_rulelevellookup"
        },
        diseaselookup:         {
          delete: "pubmed.delete_diseaselookup",
          change: "pubmed.change_diseaselookup",
          add:    "pubmed.add_diseaselookup"
        },
        mutationtypelookup:    {
          add:    "pubmed.add_mutationtypelookup",
          change: "pubmed.change_mutationtypelookup",
          delete: "pubmed.delete_mutationtypelookup"
        },
        pubmed:                {
          change: "pubmed.change_pubmed",
          delete: "pubmed.delete_pubmed",
          add:    "pubmed.add_pubmed"
        },
        variantconsequencelookup: {
          change: "pubmed.change_variantconsequencelookup",
          delete: "pubmed.delete_variantconsequencelookup",
          add:    "pubmed.add_variantconsequencelookup"
        }
      },
      contenttypes: {
        contenttype: {
          add:    "contenttypes.add_contenttype",
          change: "contenttypes.change_contenttype",
          delete: "contenttypes.delete_contenttype"
        }
      },
      socialaccount: {
        socialaccount: {
          add:    "socialaccount.add_socialaccount",
          delete: "socialaccount.delete_socialaccount",
          change: "socialaccount.change_socialaccount"
        },
        socialapp:     {
          change: "socialaccount.change_socialapp",
          add:    "socialaccount.add_socialapp",
          delete: "socialaccount.delete_socialapp"
        },
        socialtoken:   {
          delete: "socialaccount.delete_socialtoken",
          change: "socialaccount.change_socialtoken",
          add:    "socialaccount.add_socialtoken"
        }
      },
      sessions:      {
        session: {
          delete: "sessions.delete_session",
          add:    "sessions.add_session",
          change: "sessions.change_session"
        }
      },
      users:         {
        user: {
          delete: "users.delete_user",
          change: "users.change_user",
          add:    "users.add_user"
        }
      },
      authtoken:     {
        token: {
          delete: "authtoken.delete_token",
          change: "authtoken.change_token",
          add:    "authtoken.add_token"
        }
      },
      auth:          {
        group:      {
          add:    "auth.add_group",
          change: "auth.change_group",
          delete: "auth.delete_group"
        },
        permission: {
          change: "auth.change_permission",
          delete: "auth.delete_permission",
          add:    "auth.add_permission"
        }
      },
      account:       {
        emailaddress:      {
          change: "account.change_emailaddress",
          delete: "account.delete_emailaddress",
          add:    "account.add_emailaddress"
        },
        emailconfirmation: {
          change: "account.change_emailconfirmation",
          add:    "account.add_emailconfirmation",
          delete: "account.delete_emailconfirmation"
        }
      },
      sites:         {
        site: {
          delete: "sites.delete_site",
          add:    "sites.add_site",
          change: "sites.change_site"
        }
      },
      admin:         {
        logentry: {
          add:    "admin.add_logentry",
          change: "admin.change_logentry",
          delete: "admin.delete_logentry"
        }
      }
    });

  //function getPermissions() {
  //  var permissions = getPermissionsList();
  //  var results = {};
  //  angular.forEach(permissions, function(permissionString) {
  //
  //    var permission = parsePermissionString(permissionString);
  //
  //    if(permission === false) { return;}
  //
  //    results[permission.app] = results[permission.app] || {};
  //    results[permission.app][permission.model] = results[permission.app][permission.model] || {};
  //
  //    results[permission.app][permission.model][permission.access] = permission.string;
  //
  //  });
  //  return results;
  //}
  //
  //function parsePermissionString(permission) {
  //  var permissionStringSplit = permission.split(/\.|_/);
  //  if(permissionStringSplit.length !== 3) {
  //    return false;
  //  }
  //
  //  return {
  //    app:    permissionStringSplit[0],
  //    model:  permissionStringSplit[2],
  //    access: permissionStringSplit[1],
  //    string: permission
  //  };
  //
  //}
  //
  //function getPermissionsList() {
  //  return [
  //    'gene.change_gene',
  //    'pubmed.delete_syntaxlookup',
  //    'gene.change_uniprotidslookup',
  //    'gene.add_lsdblookup',
  //    'gene.delete_omimidlookup',
  //    'contenttypes.add_contenttype',
  //    'pubmed.change_varianttypelookup',
  //    'pubmed.change_syntaxlookup',
  //    'gene.change_enalookup',
  //    'gene.delete_ccdsidlookup',
  //    'gene.delete_pubmedidlookup',
  //    'pubmed.add_patientoutcomeslookup',
  //    'pubmed.custom_add_mutationtypelookup',
  //    'pubmed.add_structurelookup',
  //    'socialaccount.add_socialaccount',
  //    'sessions.delete_session',
  //    'gene.delete_prevsymbollookup',
  //    'pubmed.delete_patientoutcomeslookup',
  //    'pubmed.add_rulelevellookup',
  //    'gene.delete_prevnamelookup',
  //    'pubmed.delete_diseaselookup',
  //    'users.delete_user',
  //    'gene.delete_gene',
  //    'contenttypes.change_contenttype',
  //    'authtoken.delete_token',
  //    'gene.change_genefamilyidlookup',
  //    'socialaccount.delete_socialaccount',
  //    'pubmed.add_mutationtypelookup',
  //    'authtoken.change_token',
  //    'auth.add_group',
  //    'gene.add_aliassymbollookup',
  //    'pubmed.delete_structurelookup',
  //    'gene.add_uniprotidslookup',
  //    'gene.delete_lsdblookup',
  //    'gene.change_omimidlookup',
  //    'gene.change_prevsymbollookup',
  //    'authtoken.add_token',
  //    'gene.change_pubmedidlookup',
  //    'account.change_emailaddress',
  //    'auth.change_permission',
  //    'pubmed.delete_varianttypelookup',
  //    'gene.add_omimidlookup',
  //    'pubmed.change_mutationtypelookup',
  //    'auth.delete_permission',
  //    'gene.change_genefamilylookup',
  //    'gene.delete_genefamilyidlookup',
  //    'contenttypes.delete_contenttype',
  //    'sessions.add_session',
  //    'account.change_emailconfirmation',
  //    'gene.delete_enalookup',
  //    'gene.delete_genefamilylookup',
  //    'gene.change_mgdidlookup',
  //    'pubmed.add_syntaxlookup',
  //    'pubmed.change_pubmed',
  //    'pubmed.delete_rulelevellookup',
  //    'socialaccount.change_socialapp',
  //    'gene.delete_refseqaccessionlookup',
  //    'gene.add_pubmedidlookup',
  //    'pubmed.delete_pubmed',
  //    'socialaccount.delete_socialtoken',
  //    'sites.delete_site',
  //    'account.delete_emailaddress',
  //    'pubmed.add_varianttypelookup',
  //    'admin.add_logentry',
  //    'auth.change_group',
  //    'gene.add_enzymeidlookup',
  //    'gene.change_enzymeidlookup',
  //    'pubmed.delete_mutationtypelookup',
  //    'users.change_user',
  //    'gene.add_rgdidlookup',
  //    'gene.delete_aliassymbollookup',
  //    'sessions.change_session',
  //    'gene.change_rgdidlookup',
  //    'gene.add_genefamilylookup',
  //    'pubmed.custom_add_structurelookup',
  //    'pubmed.change_variantconsequencelookup',
  //    'sites.add_site',
  //    'pubmed.change_structurelookup',
  //    'socialaccount.add_socialapp',
  //    'gene.add_enalookup',
  //    'account.add_emailaddress',
  //    'gene.delete_rgdidlookup',
  //    'gene.add_prevsymbollookup',
  //    'users.add_user',
  //    'pubmed.delete_variantconsequencelookup',
  //    'gene.change_ccdsidlookup',
  //    'gene.add_aliasnamelookup',
  //    'gene.delete_uniprotidslookup',
  //    'gene.add_genefamilyidlookup',
  //    'pubmed.change_diseaselookup',
  //    'account.add_emailconfirmation',
  //    'account.delete_emailconfirmation',
  //    'gene.change_prevnamelookup',
  //    'socialaccount.change_socialtoken',
  //    'gene.change_lsdblookup',
  //    'gene.add_mgdidlookup',
  //    'sites.change_site',
  //    'pubmed.add_variantconsequencelookup',
  //    'gene.delete_mgdidlookup',
  //    'socialaccount.add_socialtoken',
  //    'gene.change_aliassymbollookup',
  //    'gene.add_refseqaccessionlookup',
  //    'pubmed.add_diseaselookup',
  //    'auth.delete_group',
  //    'gene.add_ccdsidlookup',
  //    'gene.delete_enzymeidlookup',
  //    'admin.change_logentry',
  //    'gene.delete_aliasnamelookup',
  //    'gene.add_gene',
  //    'pubmed.custom_change_structurelookup',
  //    'pubmed.add_pubmed',
  //    'gene.change_refseqaccessionlookup',
  //    'gene.add_prevnamelookup',
  //    'auth.add_permission',
  //    'pubmed.custom_change_mutationtypelookup',
  //    'pubmed.change_patientoutcomeslookup',
  //    'socialaccount.change_socialaccount',
  //    'socialaccount.delete_socialapp',
  //    'admin.delete_logentry',
  //    'pubmed.change_rulelevellookup',
  //    'gene.change_aliasnamelookup'
  //  ];
  //}
})();

