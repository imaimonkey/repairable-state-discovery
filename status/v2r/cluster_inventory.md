# V2R cluster inventory

2026-09-23T21:28:37.829574+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325719191552 available bytes; 81.83% used; 112501436 free inodes.

server1 `/home`: 325719191552 available bytes; 81.83% used; 112501436 free inodes.

server1 `/tmp`: 325719191552 available bytes; 81.83% used; 112501436 free inodes.

server1 `/var/tmp`: 325719191552 available bytes; 81.83% used; 112501436 free inodes.

server1 `/mnt/raid5`: 1388136112128 available bytes; 93.63% used; 337739954 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41126535168 available bytes; 97.71% used; 110432686 free inodes.

server2 `/home`: 41126535168 available bytes; 97.71% used; 110432686 free inodes.

server2 `/tmp`: 41126535168 available bytes; 97.71% used; 110432686 free inodes.

server2 `/var/tmp`: 41126535168 available bytes; 97.71% used; 110432686 free inodes.

server2 `/mnt/raid5`: 538572795904 available bytes; 96.28% used; 445208660 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293256273920 available bytes; 83.64% used; 114228993 free inodes.

server3 `/home`: 293256273920 available bytes; 83.64% used; 114228993 free inodes.

server3 `/data`: 52281073664 available bytes; 99.28% used; 225848832 free inodes.

server3 `/tmp`: 293256273920 available bytes; 83.64% used; 114228993 free inodes.

server3 `/var/tmp`: 293256273920 available bytes; 83.64% used; 114228993 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106481950720 available bytes; 94.06% used; 114356005 free inodes.

server4 `/home`: 106481950720 available bytes; 94.06% used; 114356005 free inodes.

server4 `/data`: 300336332800 available bytes; 95.85% used; 225451214 free inodes.

server4 `/tmp`: 106481950720 available bytes; 94.06% used; 114356005 free inodes.

server4 `/var/tmp`: 106481950720 available bytes; 94.06% used; 114356005 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
