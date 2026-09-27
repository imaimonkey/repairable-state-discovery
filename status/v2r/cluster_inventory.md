# V2R cluster inventory

2026-09-27T12:31:13.877171+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304683847680 available bytes; 83.00% used; 112401419 free inodes.

server1 `/home`: 304683847680 available bytes; 83.00% used; 112401419 free inodes.

server1 `/tmp`: 304683847680 available bytes; 83.00% used; 112401419 free inodes.

server1 `/var/tmp`: 304683847680 available bytes; 83.00% used; 112401419 free inodes.

server1 `/mnt/raid5`: 634592825344 available bytes; 97.09% used; 337424230 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 13440131072 available bytes; 99.25% used; 110352637 free inodes.

server2 `/home`: 13440131072 available bytes; 99.25% used; 110352637 free inodes.

server2 `/tmp`: 13440131072 available bytes; 99.25% used; 110352637 free inodes.

server2 `/var/tmp`: 13440131072 available bytes; 99.25% used; 110352637 free inodes.

server2 `/mnt/raid5`: 567368253440 available bytes; 96.08% used; 444735480 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78543704064 available bytes; 95.62% used; 114062860 free inodes.

server3 `/home`: 78543704064 available bytes; 95.62% used; 114062860 free inodes.

server3 `/data`: 1331761381376 available bytes; 81.59% used; 225758260 free inodes.

server3 `/tmp`: 78543704064 available bytes; 95.62% used; 114062860 free inodes.

server3 `/var/tmp`: 78543704064 available bytes; 95.62% used; 114062860 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111020232704 available bytes; 93.80% used; 114372805 free inodes.

server4 `/home`: 111020232704 available bytes; 93.80% used; 114372805 free inodes.

server4 `/data`: 352263520256 available bytes; 95.13% used; 224727882 free inodes.

server4 `/tmp`: 111020232704 available bytes; 93.80% used; 114372805 free inodes.

server4 `/var/tmp`: 111020232704 available bytes; 93.80% used; 114372805 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
