# V2R cluster inventory

2026-09-24T07:49:44.558497+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324422959104 available bytes; 81.90% used; 112490865 free inodes.

server1 `/home`: 324422959104 available bytes; 81.90% used; 112490865 free inodes.

server1 `/tmp`: 324422959104 available bytes; 81.90% used; 112490865 free inodes.

server1 `/var/tmp`: 324422959104 available bytes; 81.90% used; 112490865 free inodes.

server1 `/mnt/raid5`: 510049951744 available bytes; 97.66% used; 337722542 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 57830260736 available bytes; 96.77% used; 110431108 free inodes.

server2 `/home`: 57830260736 available bytes; 96.77% used; 110431108 free inodes.

server2 `/tmp`: 57830260736 available bytes; 96.77% used; 110431108 free inodes.

server2 `/var/tmp`: 57830260736 available bytes; 96.77% used; 110431108 free inodes.

server2 `/mnt/raid5`: 517694742528 available bytes; 96.42% used; 445181136 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 127170269184 available bytes; 92.90% used; 114199954 free inodes.

server3 `/home`: 127170269184 available bytes; 92.90% used; 114199954 free inodes.

server3 `/data`: 136624848896 available bytes; 98.11% used; 225839245 free inodes.

server3 `/tmp`: 127170269184 available bytes; 92.90% used; 114199954 free inodes.

server3 `/var/tmp`: 127170269184 available bytes; 92.90% used; 114199954 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105779810304 available bytes; 94.10% used; 114349172 free inodes.

server4 `/home`: 105779810304 available bytes; 94.10% used; 114349172 free inodes.

server4 `/data`: 284443660288 available bytes; 96.07% used; 225366628 free inodes.

server4 `/tmp`: 105779810304 available bytes; 94.10% used; 114349172 free inodes.

server4 `/var/tmp`: 105779810304 available bytes; 94.10% used; 114349172 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
