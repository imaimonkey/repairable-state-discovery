# V2R cluster inventory

2026-09-23T20:07:10.720109+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['3', '4', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325738737664 available bytes; 81.83% used; 112501843 free inodes.

server1 `/home`: 325738737664 available bytes; 81.83% used; 112501843 free inodes.

server1 `/tmp`: 325738737664 available bytes; 81.83% used; 112501843 free inodes.

server1 `/var/tmp`: 325738737664 available bytes; 81.83% used; 112501843 free inodes.

server1 `/mnt/raid5`: 1388964474880 available bytes; 93.63% used; 337741139 free inodes.
| server2 | True | ['6', '7'] | [] | reference_compatible=False |

server2 `/`: 41270521856 available bytes; 97.70% used; 110434884 free inodes.

server2 `/home`: 41270521856 available bytes; 97.70% used; 110434884 free inodes.

server2 `/tmp`: 41270521856 available bytes; 97.70% used; 110434884 free inodes.

server2 `/var/tmp`: 41270521856 available bytes; 97.70% used; 110434884 free inodes.

server2 `/mnt/raid5`: 541604900864 available bytes; 96.26% used; 445211444 free inodes.
| server3 | True | ['2'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293178019840 available bytes; 83.64% used; 114219194 free inodes.

server3 `/home`: 293178019840 available bytes; 83.64% used; 114219194 free inodes.

server3 `/data`: 52631744512 available bytes; 99.27% used; 225844502 free inodes.

server3 `/tmp`: 293178019840 available bytes; 83.64% used; 114219194 free inodes.

server3 `/var/tmp`: 293178019840 available bytes; 83.64% used; 114219194 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106528792576 available bytes; 94.06% used; 114356233 free inodes.

server4 `/home`: 106528792576 available bytes; 94.06% used; 114356233 free inodes.

server4 `/data`: 3055616 available bytes; 100.00% used; 225457630 free inodes.

server4 `/tmp`: 106528792576 available bytes; 94.06% used; 114356233 free inodes.

server4 `/var/tmp`: 106528792576 available bytes; 94.06% used; 114356233 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
