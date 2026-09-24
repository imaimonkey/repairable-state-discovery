# V2R cluster inventory

2026-09-24T06:35:05.904431+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324503339008 available bytes; 81.90% used; 112491614 free inodes.

server1 `/home`: 324503339008 available bytes; 81.90% used; 112491614 free inodes.

server1 `/tmp`: 324503339008 available bytes; 81.90% used; 112491614 free inodes.

server1 `/var/tmp`: 324503339008 available bytes; 81.90% used; 112491614 free inodes.

server1 `/mnt/raid5`: 517585215488 available bytes; 97.63% used; 337723751 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57882591232 available bytes; 96.77% used; 110431209 free inodes.

server2 `/home`: 57882591232 available bytes; 96.77% used; 110431209 free inodes.

server2 `/tmp`: 57882591232 available bytes; 96.77% used; 110431209 free inodes.

server2 `/var/tmp`: 57882591232 available bytes; 96.77% used; 110431209 free inodes.

server2 `/mnt/raid5`: 519544598528 available bytes; 96.41% used; 445191613 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126915383296 available bytes; 92.92% used; 114195218 free inodes.

server3 `/home`: 126915383296 available bytes; 92.92% used; 114195218 free inodes.

server3 `/data`: 139432124416 available bytes; 98.07% used; 225835649 free inodes.

server3 `/tmp`: 126915383296 available bytes; 92.92% used; 114195218 free inodes.

server3 `/var/tmp`: 126915383296 available bytes; 92.92% used; 114195218 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105805131776 available bytes; 94.10% used; 114349266 free inodes.

server4 `/home`: 105805131776 available bytes; 94.10% used; 114349266 free inodes.

server4 `/data`: 324764696576 available bytes; 95.51% used; 225372562 free inodes.

server4 `/tmp`: 105805131776 available bytes; 94.10% used; 114349266 free inodes.

server4 `/var/tmp`: 105805131776 available bytes; 94.10% used; 114349266 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
