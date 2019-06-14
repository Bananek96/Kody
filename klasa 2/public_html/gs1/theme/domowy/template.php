<?php if(!defined('IN_GS')){ die('you cannot load this page directly.'); } ?>


<script src="<?php get_theme_url(); ?>/js/jquery.min.js"></script>
<?php include("header.inc.php")?>


<body id="<?php get_page_slug(); ?>">

  <?php include("nav.inc.php"); ?>

  <!-- Treść główna -->
  <div class="container-wrapper">
    <div class="container text-center">
      <h1><?php get_page_title(); ?></h1>
      <?php get_page_content(); ?>
    </div>
    <div class="col-sm-4">
      <?php get_component('sidebar'); ?>
    </div>
  </div>

</main><!-- /.container -->

  <?php include("footer.inc.php")?>

  <!-- jQuery library -->
<script src="<?php get_theme_url(); ?>/js/popper.min.js"></script>
<script src="<?php get_theme_url(); ?>/js/bootstrap.min.js"></script>

</body>
</html>
