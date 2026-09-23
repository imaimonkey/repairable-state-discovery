# V2R cluster inventory

2026-09-23T20:57:55.497703+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325725253632 available bytes; 81.83% used; 112501591 free inodes.

server1 `/home`: 325725253632 available bytes; 81.83% used; 112501591 free inodes.

server1 `/tmp`: 325725253632 available bytes; 81.83% used; 112501591 free inodes.

server1 `/var/tmp`: 325725253632 available bytes; 81.83% used; 112501591 free inodes.

server1 `/mnt/raid5`: 1388148338688 available bytes; 93.63% used; 337740017 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41125928960 available bytes; 97.71% used; 110432729 free inodes.

server2 `/home`: 41125928960 available bytes; 97.71% used; 110432729 free inodes.

server2 `/tmp`: 41125928960 available bytes; 97.71% used; 110432729 free inodes.

server2 `/var/tmp`: 41125928960 available bytes; 97.71% used; 110432729 free inodes.

server2 `/mnt/raid5`: 539529093120 available bytes; 96.27% used; 445209582 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293463597056 available bytes; 83.62% used; 114237304 free inodes.

server3 `/home`: 293463597056 available bytes; 83.62% used; 114237304 free inodes.

server3 `/data`: 52613906432 available bytes; 99.27% used; 225850533 free inodes.

server3 `/tmp`: 293463597056 available bytes; 83.62% used; 114237304 free inodes.

server3 `/var/tmp`: 293463597056 available bytes; 83.62% used; 114237304 free inodes.
| server4 | True | ['2', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106501308416 available bytes; 94.06% used; 114356068 free inodes.

server4 `/home`: 106501308416 available bytes; 94.06% used; 114356068 free inodes.

server4 `/data`: 300589613056 available bytes; 95.85% used; 225457408 free inodes.

server4 `/tmp`: 106501308416 available bytes; 94.06% used; 114356068 free inodes.

server4 `/var/tmp`: 106501308416 available bytes; 94.06% used; 114356068 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
