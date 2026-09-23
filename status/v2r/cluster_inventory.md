# V2R cluster inventory

2026-09-23T20:19:45.941847+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['3', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325740556288 available bytes; 81.83% used; 112501843 free inodes.

server1 `/home`: 325740556288 available bytes; 81.83% used; 112501843 free inodes.

server1 `/tmp`: 325740556288 available bytes; 81.83% used; 112501843 free inodes.

server1 `/var/tmp`: 325740556288 available bytes; 81.83% used; 112501843 free inodes.

server1 `/mnt/raid5`: 1388298690560 available bytes; 93.63% used; 337741061 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 41269387264 available bytes; 97.70% used; 110434868 free inodes.

server2 `/home`: 41269387264 available bytes; 97.70% used; 110434868 free inodes.

server2 `/tmp`: 41269387264 available bytes; 97.70% used; 110434868 free inodes.

server2 `/var/tmp`: 41269387264 available bytes; 97.70% used; 110434868 free inodes.

server2 `/mnt/raid5`: 541246459904 available bytes; 96.26% used; 445210956 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 293454237696 available bytes; 83.62% used; 114234942 free inodes.

server3 `/home`: 293454237696 available bytes; 83.62% used; 114234942 free inodes.

server3 `/data`: 52606595072 available bytes; 99.27% used; 225843901 free inodes.

server3 `/tmp`: 293454237696 available bytes; 83.62% used; 114234942 free inodes.

server3 `/var/tmp`: 293454237696 available bytes; 83.62% used; 114234942 free inodes.
| server4 | True | ['0', '1', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106528055296 available bytes; 94.06% used; 114356224 free inodes.

server4 `/home`: 106528055296 available bytes; 94.06% used; 114356224 free inodes.

server4 `/data`: 7319552 available bytes; 100.00% used; 225457631 free inodes.

server4 `/tmp`: 106528055296 available bytes; 94.06% used; 114356224 free inodes.

server4 `/var/tmp`: 106528055296 available bytes; 94.06% used; 114356224 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
