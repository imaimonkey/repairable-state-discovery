# V2R cluster inventory

2026-09-25T09:41:51.098316+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318836715520 available bytes; 82.21% used; 112480389 free inodes.

server1 `/home`: 318836715520 available bytes; 82.21% used; 112480389 free inodes.

server1 `/tmp`: 318836715520 available bytes; 82.21% used; 112480389 free inodes.

server1 `/var/tmp`: 318836715520 available bytes; 82.21% used; 112480389 free inodes.

server1 `/mnt/raid5`: 350362963968 available bytes; 98.39% used; 337556846 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22836846592 available bytes; 98.73% used; 110410484 free inodes.

server2 `/home`: 22836846592 available bytes; 98.73% used; 110410484 free inodes.

server2 `/tmp`: 22836846592 available bytes; 98.73% used; 110410484 free inodes.

server2 `/var/tmp`: 22836846592 available bytes; 98.73% used; 110410484 free inodes.

server2 `/mnt/raid5`: 331402452992 available bytes; 97.71% used; 445092278 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84418088960 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84418088960 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 142296125440 available bytes; 98.03% used; 225810462 free inodes.

server3 `/tmp`: 84418088960 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84418088960 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105623396352 available bytes; 94.11% used; 114350293 free inodes.

server4 `/home`: 105623396352 available bytes; 94.11% used; 114350293 free inodes.

server4 `/data`: 240106754048 available bytes; 96.68% used; 224994035 free inodes.

server4 `/tmp`: 105623396352 available bytes; 94.11% used; 114350293 free inodes.

server4 `/var/tmp`: 105623396352 available bytes; 94.11% used; 114350293 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
