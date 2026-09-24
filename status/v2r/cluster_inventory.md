# V2R cluster inventory

2026-09-24T01:11:10.533585+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325488459776 available bytes; 81.84% used; 112499934 free inodes.

server1 `/home`: 325488459776 available bytes; 81.84% used; 112499934 free inodes.

server1 `/tmp`: 325488459776 available bytes; 81.84% used; 112499934 free inodes.

server1 `/var/tmp`: 325488459776 available bytes; 81.84% used; 112499934 free inodes.

server1 `/mnt/raid5`: 973933813760 available bytes; 95.53% used; 337734180 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40964882432 available bytes; 97.71% used; 110432135 free inodes.

server2 `/home`: 40964882432 available bytes; 97.71% used; 110432135 free inodes.

server2 `/tmp`: 40964882432 available bytes; 97.71% used; 110432135 free inodes.

server2 `/var/tmp`: 40964882432 available bytes; 97.71% used; 110432135 free inodes.

server2 `/mnt/raid5`: 531503312896 available bytes; 96.33% used; 445201911 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292627877888 available bytes; 83.67% used; 114208448 free inodes.

server3 `/home`: 292627877888 available bytes; 83.67% used; 114208448 free inodes.

server3 `/data`: 82081054720 available bytes; 98.87% used; 225843056 free inodes.

server3 `/tmp`: 292627877888 available bytes; 83.67% used; 114208448 free inodes.

server3 `/var/tmp`: 292627877888 available bytes; 83.67% used; 114208448 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106001551360 available bytes; 94.08% used; 114349234 free inodes.

server4 `/home`: 106001551360 available bytes; 94.08% used; 114349234 free inodes.

server4 `/data`: 292718428160 available bytes; 95.95% used; 225405369 free inodes.

server4 `/tmp`: 106001551360 available bytes; 94.08% used; 114349234 free inodes.

server4 `/var/tmp`: 106001551360 available bytes; 94.08% used; 114349234 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
