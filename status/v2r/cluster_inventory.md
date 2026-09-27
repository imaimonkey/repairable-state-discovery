# V2R cluster inventory

2026-09-27T13:53:39.326956+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304763883520 available bytes; 83.00% used; 112401383 free inodes.

server1 `/home`: 304763883520 available bytes; 83.00% used; 112401383 free inodes.

server1 `/tmp`: 304763883520 available bytes; 83.00% used; 112401383 free inodes.

server1 `/var/tmp`: 304763883520 available bytes; 83.00% used; 112401383 free inodes.

server1 `/mnt/raid5`: 634876268544 available bytes; 97.09% used; 337424252 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 13415878656 available bytes; 99.25% used; 110351820 free inodes.

server2 `/home`: 13415878656 available bytes; 99.25% used; 110351820 free inodes.

server2 `/tmp`: 13415878656 available bytes; 99.25% used; 110351820 free inodes.

server2 `/var/tmp`: 13415878656 available bytes; 99.25% used; 110351820 free inodes.

server2 `/mnt/raid5`: 528018952192 available bytes; 96.35% used; 444732687 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78563262464 available bytes; 95.62% used; 114062773 free inodes.

server3 `/home`: 78563262464 available bytes; 95.62% used; 114062773 free inodes.

server3 `/data`: 1330870218752 available bytes; 81.61% used; 225757292 free inodes.

server3 `/tmp`: 78563262464 available bytes; 95.62% used; 114062773 free inodes.

server3 `/var/tmp`: 78563262464 available bytes; 95.62% used; 114062773 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111009873920 available bytes; 93.81% used; 114372795 free inodes.

server4 `/home`: 111009873920 available bytes; 93.81% used; 114372795 free inodes.

server4 `/data`: 350931099648 available bytes; 95.15% used; 224727468 free inodes.

server4 `/tmp`: 111009873920 available bytes; 93.81% used; 114372795 free inodes.

server4 `/var/tmp`: 111009873920 available bytes; 93.81% used; 114372795 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
