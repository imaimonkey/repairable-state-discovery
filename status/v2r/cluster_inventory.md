# V2R cluster inventory

2026-09-24T03:25:13.538104+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325357080576 available bytes; 81.85% used; 112498204 free inodes.

server1 `/home`: 325357080576 available bytes; 81.85% used; 112498204 free inodes.

server1 `/tmp`: 325357080576 available bytes; 81.85% used; 112498204 free inodes.

server1 `/var/tmp`: 325357080576 available bytes; 81.85% used; 112498204 free inodes.

server1 `/mnt/raid5`: 420075184128 available bytes; 98.07% used; 337733083 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40843202560 available bytes; 97.72% used; 110431134 free inodes.

server2 `/home`: 40843202560 available bytes; 97.72% used; 110431134 free inodes.

server2 `/tmp`: 40843202560 available bytes; 97.72% used; 110431134 free inodes.

server2 `/var/tmp`: 40843202560 available bytes; 97.72% used; 110431134 free inodes.

server2 `/mnt/raid5`: 527325913088 available bytes; 96.36% used; 445198340 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292379766784 available bytes; 83.68% used; 114201090 free inodes.

server3 `/home`: 292379766784 available bytes; 83.68% used; 114201090 free inodes.

server3 `/data`: 38836682752 available bytes; 99.46% used; 225843216 free inodes.

server3 `/tmp`: 292379766784 available bytes; 83.68% used; 114201090 free inodes.

server3 `/var/tmp`: 292379766784 available bytes; 83.68% used; 114201090 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105987309568 available bytes; 94.09% used; 114349611 free inodes.

server4 `/home`: 105987309568 available bytes; 94.09% used; 114349611 free inodes.

server4 `/data`: 285740126208 available bytes; 96.05% used; 225386237 free inodes.

server4 `/tmp`: 105987309568 available bytes; 94.09% used; 114349611 free inodes.

server4 `/var/tmp`: 105987309568 available bytes; 94.09% used; 114349611 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
