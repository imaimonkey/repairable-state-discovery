# V2R cluster inventory

2026-09-27T12:09:53.297732+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304692383744 available bytes; 83.00% used; 112401514 free inodes.

server1 `/home`: 304692383744 available bytes; 83.00% used; 112401514 free inodes.

server1 `/tmp`: 304692383744 available bytes; 83.00% used; 112401514 free inodes.

server1 `/var/tmp`: 304692383744 available bytes; 83.00% used; 112401514 free inodes.

server1 `/mnt/raid5`: 634682892288 available bytes; 97.09% used; 337424376 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16407810048 available bytes; 99.08% used; 110352888 free inodes.

server2 `/home`: 16407810048 available bytes; 99.08% used; 110352888 free inodes.

server2 `/tmp`: 16407810048 available bytes; 99.08% used; 110352888 free inodes.

server2 `/var/tmp`: 16407810048 available bytes; 99.08% used; 110352888 free inodes.

server2 `/mnt/raid5`: 569030246400 available bytes; 96.07% used; 444735795 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78542856192 available bytes; 95.62% used; 114062864 free inodes.

server3 `/home`: 78542856192 available bytes; 95.62% used; 114062864 free inodes.

server3 `/data`: 1331799146496 available bytes; 81.59% used; 225758583 free inodes.

server3 `/tmp`: 78542856192 available bytes; 95.62% used; 114062864 free inodes.

server3 `/var/tmp`: 78542856192 available bytes; 95.62% used; 114062864 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111029141504 available bytes; 93.80% used; 114372805 free inodes.

server4 `/home`: 111029141504 available bytes; 93.80% used; 114372805 free inodes.

server4 `/data`: 352656941056 available bytes; 95.13% used; 224727987 free inodes.

server4 `/tmp`: 111029141504 available bytes; 93.80% used; 114372805 free inodes.

server4 `/var/tmp`: 111029141504 available bytes; 93.80% used; 114372805 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
