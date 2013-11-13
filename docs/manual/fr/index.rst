.. -*- coding: utf-8 -*-

==============================================================================================================
Présentation des fonctionnalités possibles d'un annuaire dans un système d'information collaboratif sous Plone
==============================================================================================================

La suite `collective.contact.*` est constituée de plusieurs modules permettant de créer et de gérer un annuaire dans un portail Plone. Ce document donne un aperçu des principales fonctionnalités fournies par cette suite.

.. add toctree ?

Créer un contenu "annuaire"
===========================

Un système d'information collaboratif sous Plone contient par défaut un seul annuaire. Cet annuaire permet de gérer des organisations et des fonctions en liaison avec des personnes physiques.
Il est possible de définir des types d'organisation, des niveaux d'organisation et des types de fonctions spécifiques.

Pour créer un annuaire, il convient de commencer par ajouter un contenu "Annuaire" dans votre système d'information collaboratif sous Plone et de remplir les champs suivants :

.. figure:: ./images/add_directory.png
    :align: center


Ajouter une personne dans l'annuaire
====================================

Une fois le contenu "Annuaire" créé, des personnes peuvent être ajoutées :

.. figure:: ./images/mdurand.png
    :align: center

Comme nous le verrons plus tard, une personne peut occuper une ou plusieurs fonctions dans une ou plusieurs organisations.


Ajouter une organisation dans l'annuaire
========================================

Tout d'abord, ajoutons l'organisation Dorémi de type entreprise dans l'annuaire :

.. figure:: ./images/add_organization.png
    :align: center

L'utilisateur clique sur l'onglet coordonnées :

.. figure:: ./images/contact_info_form.png
    :align: center

.. figure:: ./images/address_form.png
    :align: center

L'adresse de l'entreprise sera utilisée comme adresse par défaut pour toutes les organisations et toutes les fonctions qui seront ajoutées dans celle-ci.


Ajouter une fonction dans une organisation
==========================================

Nous pouvons maintenant ajouter une fonction "Président directeur général" pour cette société :

.. figure:: ./images/add_position.png
    :align: center

On retrouve l'adresse saisie pour l'entreprise :

.. figure:: ./images/position_parent_address.png
    :align: center

Il reste toutefois possible d'attribuer une adresse différente à la fonction en décochant "Utiliser l'adresse de l'entité d'appartenance" :

.. figure:: ./images/position_own_address.png
    :align: center



Associer une personne à une fonction
====================================

Sur la fiche de cette fonction, un lien permet de créer un contact associé à cette fonction :

.. figure:: ./images/add_contact_link.png
    :align: center

Les champs "Organisation" et "Fonction" sont préremplis dans le formulaire d'ajout du contact :

.. figure:: ./images/contact_overlay_before.png
    :align: center


Au survol d'une organisation, une "tooltip" permet d'avoir un aperçu des informations la concernant :

.. figure:: ./images/tooltip_orga.png
    :align: center


Nous pouvons alors associer une personne déjà présente dans l'annuaire à cette fonction à l'aide d'un champ autocomplété :

.. figure:: ./images/person_autocomplete.png
    :align: center

Ou créer une nouvelle personne (sans perdre les informations préremplies (organisation et fonction) pour le contact) :

.. figure:: ./images/add_person_in_overlay.png
    :align: center


La personne créée via ce formulaire est automatiquement sélectionnée pour le champ "Personne" du formulaire d'ajout de contact :

.. figure:: ./images/contact_overlay_after.png
    :align: center

Le contact est créé et nous pouvons aller sur sa fiche afin de télécharger sa vcard (vcard est un standard qui permet de représenter les informations de contact) :

.. figure:: ./images/download_vcard_link.png
    :align: center

.. todo? ./images/vcard.png


Sous-organisations
==================

Créons l'organigramme de cette société. Il s'agit d'une PME comprenant deux équipes :

.. figure:: ./images/team_marketing.png
    :align: center

.. figure:: ./images/team_dev.png
    :align: center

Tout comme la fonction PDG, les équipes héritent de l'adresse de l'organisation par défaut :

.. figure:: ./images/position_parent_address.png
    :align: center

Nous pouvons désormais continuer à détailler l'organigramme de Dorémi en ajoutant des fonctions dans les équipes, en créant d'autres niveaux d'organisation ou même créer d'autres organisations (associations, entreprises, ...) à la racine de l'annuaire.

La fiche de l'organisation permet d'avoir une vue synthétique de l'organigramme :

.. figure:: ./images/orga_page.png
    :align: center
