# V2R cluster inventory

2026-09-27T11:19:37.566230+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304693080064 available bytes; 83.00% used; 112401646 free inodes.

server1 `/home`: 304693080064 available bytes; 83.00% used; 112401646 free inodes.

server1 `/tmp`: 304693080064 available bytes; 83.00% used; 112401646 free inodes.

server1 `/var/tmp`: 304693080064 available bytes; 83.00% used; 112401646 free inodes.

server1 `/mnt/raid5`: 635402321920 available bytes; 97.09% used; 337424414 free inodes.
| server2 | True | ['2', '7'] | [] | reference_compatible=False |

server2 `/`: 16433827840 available bytes; 99.08% used; 110353150 free inodes.

server2 `/home`: 16433827840 available bytes; 99.08% used; 110353150 free inodes.

server2 `/tmp`: 16433827840 available bytes; 99.08% used; 110353150 free inodes.

server2 `/var/tmp`: 16433827840 available bytes; 99.08% used; 110353150 free inodes.

server2 `/mnt/raid5`: 569961275392 available bytes; 96.06% used; 444737235 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78544068608 available bytes; 95.62% used; 114062817 free inodes.

server3 `/home`: 78544068608 available bytes; 95.62% used; 114062817 free inodes.

server3 `/data`: 1331996200960 available bytes; 81.59% used; 225759714 free inodes.

server3 `/tmp`: 78544068608 available bytes; 95.62% used; 114062817 free inodes.

server3 `/var/tmp`: 78544068608 available bytes; 95.62% used; 114062817 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111030493184 available bytes; 93.80% used; 114372817 free inodes.

server4 `/home`: 111030493184 available bytes; 93.80% used; 114372817 free inodes.

server4 `/data`: 353684422656 available bytes; 95.11% used; 224728223 free inodes.

server4 `/tmp`: 111030493184 available bytes; 93.80% used; 114372817 free inodes.

server4 `/var/tmp`: 111030493184 available bytes; 93.80% used; 114372817 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
