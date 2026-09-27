# V2R cluster inventory

2026-09-27T04:45:02.757160+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['0', '2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314888663040 available bytes; 82.43% used; 112443031 free inodes.

server1 `/home`: 314888663040 available bytes; 82.43% used; 112443031 free inodes.

server1 `/tmp`: 314888663040 available bytes; 82.43% used; 112443031 free inodes.

server1 `/var/tmp`: 314888663040 available bytes; 82.43% used; 112443031 free inodes.

server1 `/mnt/raid5`: 636058292224 available bytes; 97.08% used; 337400333 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17627467776 available bytes; 99.02% used; 110365000 free inodes.

server2 `/home`: 17627467776 available bytes; 99.02% used; 110365000 free inodes.

server2 `/tmp`: 17627467776 available bytes; 99.02% used; 110365000 free inodes.

server2 `/var/tmp`: 17627467776 available bytes; 99.02% used; 110365000 free inodes.

server2 `/mnt/raid5`: 576404795392 available bytes; 96.02% used; 444879079 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78695964672 available bytes; 95.61% used; 114062923 free inodes.

server3 `/home`: 78695964672 available bytes; 95.61% used; 114062923 free inodes.

server3 `/data`: 1334006411264 available bytes; 81.56% used; 225759000 free inodes.

server3 `/tmp`: 78695964672 available bytes; 95.61% used; 114062923 free inodes.

server3 `/var/tmp`: 78695964672 available bytes; 95.61% used; 114062923 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111009370112 available bytes; 93.81% used; 114372934 free inodes.

server4 `/home`: 111009370112 available bytes; 93.81% used; 114372934 free inodes.

server4 `/data`: 382111289344 available bytes; 94.72% used; 224780546 free inodes.

server4 `/tmp`: 111009370112 available bytes; 93.81% used; 114372934 free inodes.

server4 `/var/tmp`: 111009370112 available bytes; 93.81% used; 114372934 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
