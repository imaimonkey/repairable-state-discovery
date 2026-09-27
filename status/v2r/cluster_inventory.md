# V2R cluster inventory

2026-09-27T00:41:18.657886+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 315146448896 available bytes; 82.42% used; 112443471 free inodes.

server1 `/home`: 315146448896 available bytes; 82.42% used; 112443471 free inodes.

server1 `/tmp`: 315146448896 available bytes; 82.42% used; 112443471 free inodes.

server1 `/var/tmp`: 315146448896 available bytes; 82.42% used; 112443471 free inodes.

server1 `/mnt/raid5`: 637679779840 available bytes; 97.07% used; 337407670 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17624104960 available bytes; 99.02% used; 110365012 free inodes.

server2 `/home`: 17624104960 available bytes; 99.02% used; 110365012 free inodes.

server2 `/tmp`: 17624104960 available bytes; 99.02% used; 110365012 free inodes.

server2 `/var/tmp`: 17624104960 available bytes; 99.02% used; 110365012 free inodes.

server2 `/mnt/raid5`: 592887894016 available bytes; 95.90% used; 444956696 free inodes.
| server3 | True | ['0', '3'] | [] | reference_compatible=True |

server3 `/`: 79497388032 available bytes; 95.56% used; 114068710 free inodes.

server3 `/home`: 79497388032 available bytes; 95.56% used; 114068710 free inodes.

server3 `/data`: 1348971622400 available bytes; 81.36% used; 225825434 free inodes.

server3 `/tmp`: 79497388032 available bytes; 95.56% used; 114068710 free inodes.

server3 `/var/tmp`: 79497388032 available bytes; 95.56% used; 114068710 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105879027712 available bytes; 94.09% used; 114347836 free inodes.

server4 `/home`: 105879027712 available bytes; 94.09% used; 114347836 free inodes.

server4 `/data`: 409211211776 available bytes; 94.34% used; 224820611 free inodes.

server4 `/tmp`: 105879027712 available bytes; 94.09% used; 114347836 free inodes.

server4 `/var/tmp`: 105879027712 available bytes; 94.09% used; 114347836 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
