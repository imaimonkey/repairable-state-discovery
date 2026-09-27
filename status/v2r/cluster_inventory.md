# V2R cluster inventory

2026-09-27T12:38:51.202190+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304682975232 available bytes; 83.00% used; 112401392 free inodes.

server1 `/home`: 304682975232 available bytes; 83.00% used; 112401392 free inodes.

server1 `/tmp`: 304682975232 available bytes; 83.00% used; 112401392 free inodes.

server1 `/var/tmp`: 304682975232 available bytes; 83.00% used; 112401392 free inodes.

server1 `/mnt/raid5`: 634592321536 available bytes; 97.09% used; 337424227 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 13428981760 available bytes; 99.25% used; 110352377 free inodes.

server2 `/home`: 13428981760 available bytes; 99.25% used; 110352377 free inodes.

server2 `/tmp`: 13428981760 available bytes; 99.25% used; 110352377 free inodes.

server2 `/var/tmp`: 13428981760 available bytes; 99.25% used; 110352377 free inodes.

server2 `/mnt/raid5`: 557901049856 available bytes; 96.15% used; 444735066 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78543523840 available bytes; 95.62% used; 114062857 free inodes.

server3 `/home`: 78543523840 available bytes; 95.62% used; 114062857 free inodes.

server3 `/data`: 1331756466176 available bytes; 81.59% used; 225758195 free inodes.

server3 `/tmp`: 78543523840 available bytes; 95.62% used; 114062857 free inodes.

server3 `/var/tmp`: 78543523840 available bytes; 95.62% used; 114062857 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111020048384 available bytes; 93.80% used; 114372805 free inodes.

server4 `/home`: 111020048384 available bytes; 93.80% used; 114372805 free inodes.

server4 `/data`: 352139091968 available bytes; 95.13% used; 224727851 free inodes.

server4 `/tmp`: 111020048384 available bytes; 93.80% used; 114372805 free inodes.

server4 `/var/tmp`: 111020048384 available bytes; 93.80% used; 114372805 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
