# V2R cluster inventory

2026-09-27T12:43:25.493121+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304683573248 available bytes; 83.00% used; 112401394 free inodes.

server1 `/home`: 304683573248 available bytes; 83.00% used; 112401394 free inodes.

server1 `/tmp`: 304683573248 available bytes; 83.00% used; 112401394 free inodes.

server1 `/var/tmp`: 304683573248 available bytes; 83.00% used; 112401394 free inodes.

server1 `/mnt/raid5`: 634591834112 available bytes; 97.09% used; 337424226 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 13427347456 available bytes; 99.25% used; 110352294 free inodes.

server2 `/home`: 13427347456 available bytes; 99.25% used; 110352294 free inodes.

server2 `/tmp`: 13427347456 available bytes; 99.25% used; 110352294 free inodes.

server2 `/var/tmp`: 13427347456 available bytes; 99.25% used; 110352294 free inodes.

server2 `/mnt/raid5`: 557762650112 available bytes; 96.15% used; 444734776 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78534574080 available bytes; 95.62% used; 114062855 free inodes.

server3 `/home`: 78534574080 available bytes; 95.62% used; 114062855 free inodes.

server3 `/data`: 1331747012608 available bytes; 81.59% used; 225758153 free inodes.

server3 `/tmp`: 78534574080 available bytes; 95.62% used; 114062855 free inodes.

server3 `/var/tmp`: 78534574080 available bytes; 95.62% used; 114062855 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111011536896 available bytes; 93.81% used; 114372805 free inodes.

server4 `/home`: 111011536896 available bytes; 93.81% used; 114372805 free inodes.

server4 `/data`: 352057307136 available bytes; 95.13% used; 224727839 free inodes.

server4 `/tmp`: 111011536896 available bytes; 93.81% used; 114372805 free inodes.

server4 `/var/tmp`: 111011536896 available bytes; 93.81% used; 114372805 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
