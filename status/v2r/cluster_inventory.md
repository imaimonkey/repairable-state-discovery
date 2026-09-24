# V2R cluster inventory

2026-09-24T01:49:17.062183+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325454520320 available bytes; 81.84% used; 112499439 free inodes.

server1 `/home`: 325454520320 available bytes; 81.84% used; 112499439 free inodes.

server1 `/tmp`: 325454520320 available bytes; 81.84% used; 112499439 free inodes.

server1 `/var/tmp`: 325454520320 available bytes; 81.84% used; 112499439 free inodes.

server1 `/mnt/raid5`: 817631158272 available bytes; 96.25% used; 337733771 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40925114368 available bytes; 97.72% used; 110431847 free inodes.

server2 `/home`: 40925114368 available bytes; 97.72% used; 110431847 free inodes.

server2 `/tmp`: 40925114368 available bytes; 97.72% used; 110431847 free inodes.

server2 `/var/tmp`: 40925114368 available bytes; 97.72% used; 110431847 free inodes.

server2 `/mnt/raid5`: 530222567424 available bytes; 96.34% used; 445201139 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292716748800 available bytes; 83.67% used; 114210738 free inodes.

server3 `/home`: 292716748800 available bytes; 83.67% used; 114210738 free inodes.

server3 `/data`: 71098933248 available bytes; 99.02% used; 225841910 free inodes.

server3 `/tmp`: 292716748800 available bytes; 83.67% used; 114210738 free inodes.

server3 `/var/tmp`: 292716748800 available bytes; 83.67% used; 114210738 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105950560256 available bytes; 94.09% used; 114348564 free inodes.

server4 `/home`: 105950560256 available bytes; 94.09% used; 114348564 free inodes.

server4 `/data`: 289763352576 available bytes; 96.00% used; 225388489 free inodes.

server4 `/tmp`: 105950560256 available bytes; 94.09% used; 114348564 free inodes.

server4 `/var/tmp`: 105950560256 available bytes; 94.09% used; 114348564 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
